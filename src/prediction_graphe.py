import graphe as graphe
import numpy as np
import inversion as inv
import mersenne_twister as mers
import random as rand



# 629 = 20096 bits + 4 bits (les 28 autres bits sont utilisés pour generer la ligne suivante)
#31125-20100 = on doit predire 11025 bits sachant qu'on connait deja 28 bits
# on doit generer 10997 bits pour completer le graphe donc generer 344 nouveaux entiers 
#10997-10976 = on va utiliser les 21 bits 


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

    

def reconstitution_MT(matrice) :
    mt_entiers = [-1]*624
    for i in range(624):
        mt_entiers[i]= inv.inversion(inv.conversion_base10(int(matrice[i])))
    return mt_entiers


def generation_reste_graphe(Nombres):
    matrice=np.zeros((150,250))
    index = 0

    for i in range(119):
        matrice[0][i]= m1[100][i]
        if i> 100 :
            matrice[i-100][100] = m1[100][i]
       

    for i in range(1,150) :
        n= 100+i
        for j in range(0,100):
            matrice[i][j]=m1[j][n]
   

    
    for i in range(119,250):
        k=graphe.extract_bit(Nombres[index//32],index%32)
        matrice[0][i]=int(k)
        matrice[i-100][100]=int(k)
        index+=1
            
    
    for i in range(1,250) :
         n= 100+i
         for j in range(n+1,250):
             k=graphe.extract_bit(Nombres[index//32],index%32)
             matrice[i][j]=int(k)
             matrice[j-100][n]=int(k)
             index+=1
             
            
    return matrice

#Prédiction avec nos propres algorithmes
(n,m) = graphe.generate_graph()
m1 = m[0:200]
tab_entiers = reconstitution_Entiers(m1)
mt_entiers = reconstitution_MT(tab_entiers)
g = mers.generateur(mt_entiers)
g.twist()
entiers_generés = [-1]*349
for i in range (349):
    entiers_generés[i]=g.extract_number()

res=generation_reste_graphe(entiers_generés)
graphe = np.concatenate((m1[0:100],res))
print(np.array_equal(graphe,m))




