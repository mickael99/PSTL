import mersenne_twister as mt
import numpy as np
import inversion as inv


# dans le graphe complet on a besoin 31125 arrete et 31125/32 = 972.65625
# il faut generer 2 matrices de mersenne 973 entier = 624 entiers + 349 entiers 

def extract_bit(n,i) :
    return (n>>(31-i))&1


def generate_graph() :
    number = 0
    Nombres = [-1]*973
    mt.seed_mt()
    for i in range (973):
        Nombres[i]= mt.extract_number()

    matrice=np.zeros((250,250))

    index = 0

    for i in range(250) :
        for j in range(i+1,250):
            n=extract_bit(Nombres[index//32],index%32)
            matrice[i][j]=int(n)
            matrice[j][i]=int(n)
            index+=1
            if number == 31 :
                number=0
            else :
                number+=1
    
    
            
            

    return (Nombres ,matrice )


        

