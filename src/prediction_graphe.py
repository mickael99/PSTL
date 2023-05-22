import graphe as g
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
    print(mt_entiers[0])
    return mt_entiers


def twist2(MT):
    n=624
    for i in range(n):
        x = (MT[i] & mers.upper_mask) | (MT[(i  + 1) % n] & mers.lower_mask)

        xa = x >> 1
        if (x % 2) != 0:
            xa = xa ^ mers.a
        
      
        MT[i] = MT[(i + mers.m) % n] ^ xa
    return MT




def extract_number2(MT):
    entiers_predis=[-1]*349
    for i in range(349):

        y = MT[i]
    
        y = y ^ ((y >> mers.u) & mers.d)
  

        y = y ^ ((y << mers.s) & mers.b)
   
        y = y ^ ((y << mers.t) & mers.c)
        y = y ^ (y >> mers.l)

        y= y % mers.mod

        entiers_predis[i] =y


    return entiers_predis
     

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
        k=g.extract_bit(Nombres[index//32],index%32)
        matrice[0][i]=int(k)
        matrice[i-100][100]=int(k)
        index+=1
            
    
    for i in range(1,250) :
         n= 100+i
         for j in range(n+1,250):
             k=g.extract_bit(Nombres[index//32],index%32)
             matrice[i][j]=int(k)
             matrice[j-100][n]=int(k)
             index+=1
             
            
    return matrice

#Prédiction avec nos propres algorithmes
(n,m) = g.generate_graph()
m1 = m[0:200]
tab_entiers = reconstitution_Entiers(m1)
mt_entiers = reconstitution_MT(tab_entiers)
mt_entiers2=twist2(mt_entiers)
entiers_generés = extract_number2(mt_entiers2)
res=generation_reste_graphe(entiers_generés)
graphe = np.concatenate((m1[0:100],res))
print(np.array_equal(graphe,m))




