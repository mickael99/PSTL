#Si l'entrée est une chaine de caractère, La fonction seed de python convertit
#ce dernier en valeur entière pour pouvoir la manipuer et ainsi générer les graines. Seed ne
#fait rien de plus, si l'entrée est un entier, alors cette valeur ne sera pas modifié


import randomTest
import random
import numpy as np
    
w = 32
n = 624
m = 397
f = 1812433253
r = 31
u = 11
s = 7
t = 15
a = 2567483615
d = 4294967295
b = 2636928640
c = 4022730752
l= 18
mod = pow(2, w)

MT = [0] * n
index = n + 1
#31 bits à "1"
lower_mask = (1 << r) - 1
#31 bits de poids faibles à 0 et le bit de poids fort à 1 (codé sur 32 bits)
upper_mask = (~lower_mask) % mod


X0 = 9753102468



def next_int():
    ### générateur rand48
    ### renvoie un entier 32 bits, en partant de X0

    global X0

    a = 25214903917
    m = 2**48
    c= 11

    X0 = ( a * X0 + c ) % m
    return X0 >> 16

def seed_mt():
    global index
    index = n
    for i in range(n):
        MT[i] = next_int()
    



def extract_number():
    global index

    if index >= n:
        if index > n:
            print("Generator was never seeded")
            return -1
        twist()

    y = MT[index]
    
    #1- on divise y par 2^11
    #2- on effectue un "et binaire" avec le résulat de l'étape 1 et la constante "d"
    #3- y = on effectue un ou esclusif avec le résultat de l'étape 2 et l'ancien y
    y = y ^ ((y >> u) & d)
  

    #4- on multiplie y par 2^7
    #5- on effectue un "et binaire" avec le résulat de l'étape 4 et la constante "b"
    #6- y = on effectue un ou esclusif avec le résultat de l'étape 5 et l'ancien y
    y = y ^ ((y << s) & b)
   

    #7- on multiplie y par 2^15
    #8- on effectue un "et binaire" avec le résulat de l'étape 7 et la constante "c"
    #9- y = on effectue un ou esclusif avec le résultat de l'étape 8 et l'ancien y
    y = y ^ ((y << t) & c)


    #10- on divise y par 2
    #11- y = on effectue un ou esclusif avec le résultat de l'étape 10 et l'ancien y
    y = y ^ (y >> l)

    index += 1

    #12- on prend les 32 bits de poids faibles
    return y % mod

#La modification de chaque graines dépend de la valeur des autres graines du tableau
def twist():
    global index

    for i in range(n):
        # 1-Pour chaque graines, on 
        #   * on effectue le "et binaire" avec upper_mask
        #       -> si le bit de poids fort de la graine vaut 0 alors res = 0
        #       -> si le bit de poids fort de la graine vaut 1 alors res = upper_mask        
        # 2-On prend la graine suivante en explorant le tableau de manière circulaire
        #   et on effectue le "et binaire" avec lower_mask afin de séléctionner les 31 bits 
        #   de poids faible de la graine
        # 3-On effectue un "ou binaire" avec les résulats de l'étape 1 et 2
        #       -> si res de l'étape 1 = 0 alors le résulat de x sera le résultat de l'étape 2
        #       -> si res de l'étape 1 = upper_mask les 31 bits de poids faibles seront équivalents
        #          aux 31 bits de poids faibles du resultat de l'étape 2 et le 32ème bit sera à 1
        x = (MT[i] & upper_mask) | (MT[(i  + 1) % n] & lower_mask)
        #xa = x / 2
        xa = x >> 1
        #on rentre dans la condition si x est impair (si le bit de poid faible est à 1)
        # si c'est ele cas, on fait le "ou exclusif" entre xa(x / 2) et a
        if (x % 2) != 0:
            xa = xa ^ a
        
        #on récupère la valeur de la 394 + ième case en partant de l'indice où est stocké
        #la graine courante (on effectue ce parcourt de manière circulaire) puis on effectue le 
        # "ou exclusif" cette valeur et celle de xa
        MT[i] = MT[(i + m) % n] ^ xa
    #on revient à 0 une fois qu'on a modifié la totalité des graines
    index = 0
   
