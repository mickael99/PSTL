import graphe as graphe
import numpy as np
import inversion as inv
import mersenne_twister as mers
import random as rand




"""
    Permet d'obtenir les 624 premiers entiers generé par le Mersenne Twister

    @param m1: la sous-matrice du graphe
   

    @return  tab_entiers : tableau qui contient la representation binaire des 624 entiers
"""
def reconstitution_Entiers(m1) :
    tab_entiers = [""]*624
    nb =0

    for i in range(200):
        for j in range(i+1,250):
            tab_entiers[nb//32]+=str(int(m1[i][j]))
            nb+=1
            if nb >= 624*32 :
                break
        if nb >= 624*32 :
                break
    return tab_entiers

    
"""
    Permet d'obtenir le tableau de mersenne MT apres la premiere initialisation 

    @param matrice : le tableau qui contient les 624 premiers entiers
   

    @return mt_entiers:  le tableau MT initial
"""
def reconstitution_MT(matrice) :
    mt_entiers = [-1]*624
    for i in range(624):
        mt_entiers[i]= inv.inversion(inv.conversion_base10(int(matrice[i])))
    return mt_entiers

"""
    Permet d'obtenir le reste du tableau 

    @param Nombres : le tableau qui contient les 349 entiers suivants
   

    @return matrice :  la matrice d'adjasence qui represente le reste du graphe
"""
def generation_reste_graphe(Nombres):
    matrice=np.zeros((150,250))
    index = 0

# remplir la premiere colones de la premiere ligne qui correspondent au derniers entiers avant le twist
    for i in range(119):
        matrice[0][i]= m1[100][i]
        if i> 100 :
            matrice[i-100][100] = m1[100][i]
       
# remplir les cases paar la symetrie
    for i in range(1,150) :
        n= 100+i
        for j in range(0,100):
            matrice[i][j]=m1[j][n]
   

# remplir le reste de la premiere ligne avec les entiers predis
    for i in range(119,250):
        k=graphe.extract_bit(Nombres[index//32],index%32)
        matrice[0][i]=int(k)
        matrice[i-100][100]=int(k)
        index+=1
            
# remplir le reste de la maatrice avec les entiers predis
    for i in range(1,250) :
         n= 100+i
         for j in range(n+1,250):
             k=graphe.extract_bit(Nombres[index//32],index%32)
             matrice[i][j]=int(k)
             matrice[j-100][n]=int(k)
             index+=1
             
            
    return matrice


#Prédiction avec nos propres algorithmes en utilisant graphe.generate_graphe()
#utiliser graphe.generate_graphe_with_python_algo() pour tester la prediction aves un graphe generé par python
(n,m) = graphe.generate_graph()
#recuperer la sous_matrice
m1 = m[0:200]

tab_entiers = reconstitution_Entiers(m1)
mt_entiers = reconstitution_MT(tab_entiers)
g = mers.generateur(mt_entiers)
g.twist()
entiers_generés = [-1]*349
for i in range (349):
    entiers_generés[i]=g.extract_number()
res=generation_reste_graphe(entiers_generés)
#concatener la sous matrice et la matrice predite dans une matrice graphe
graphe = np.concatenate((m1[0:100],res))
#comparer graphe et la matrice initiale m 
print(np.array_equal(graphe,m))




