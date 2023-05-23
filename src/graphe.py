import mersenne_twister as mt
import numpy as np
import inversion as inv
import random as rand

"""
    Dans le graphe complet, nous avons besoin de 31125 arrete.
    31125/32 = 972.65625.
    Donc, il faut générer 2 matrices de mersenne 973 entier = 624 entiers + 349 entiers 
"""

"""
    Permet d'obtenir le i ème bit d'un entier sous sa forme binaire 

    @param n L'entier 
    @param i La position du bit à lire (Le bit de poids faible à la position 1)

    @return Le bit lu
"""
def extract_bit(n,i) :
    return (n>>(31-i))&1

"""
    Génère un graphe non orienté de 250 sommets en utilisant l'algorithme 
    de génération de nombre aléatoire proposé par python pour chaque arête

    @return Les 973 entiers tirés aléatoirement
            La matrice générée
"""
def generate_graphe_with_python_algo():
    rand.seed(mt.X0);
    Nombres = [0]*973
    matrice = np.zeros((250, 250))

    for i in range(973):
        Nombres[i] = rand.getrandbits(32)
    
        index = 0
    for i in range(250) :
        for j in range(i+1,250):
            n=extract_bit(Nombres[index//32],index%32)
            matrice[i][j]=int(n)
            matrice[j][i]=int(n)
            index+=1
         
    return (Nombres ,matrice )

"""
    Génère un graphe non orienté de 250 sommets en utilisant l'algorithme 
    de génération de nombre aléatoire que nous avions développée dans le fichier "mersenne_twister.py"

    @return Les 973 entiers tirés aléatoirement
            La matrice générée
"""   
def generate_graph() :
    Nombres = [-1]*973
    mat= [-1]*624
    mers = mt.generateur(mat)
    mers.seed_mt()
    for i in range (973):
        Nombres[i]= mers.extract_number()

    matrice=np.zeros((250,250))

    index = 0

    for i in range(250) :
        for j in range(i+1,250):
            n=extract_bit(Nombres[index//32],index%32)
            matrice[i][j]=int(n)
            matrice[j][i]=int(n)
            index+=1
          
    return (Nombres ,matrice )


        

