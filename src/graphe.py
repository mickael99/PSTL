import mersenne_twister as mt
import numpy as np

# dans le graphe complet on a besoin 19900 arrete et 19900/32 = 621.875
# il faut generer 622 entier = 621 entiers + 28 bits 

def extract_bit(n,i) :
    return (n>>i)&1


def generate_graphe() :
    
    Nombres = [-1]*622
    mt.seed_mt()
    for i in range (622):
        Nombres[i]= mt.extract_number()

    matrice=np.zeros((200,200))

    index = 0

    for i in range(200) :
        for j in range(i+1,200):
            n=extract_bit(Nombres[index//32],index%32)
            matrice[i][j]=n
            matrice[j][i]=n
            index+=1

    return(matrice , Nombres)



    




        

