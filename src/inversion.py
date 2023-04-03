t = 15
c = 4022730752
s = 7
b = 2636928640

def convert_binary(y):
    return '{:032b}'.format(y)   

def add_O(y):
    if len(y) > 32:
        print("erreur, y contient plus de 32 bits")
    elif len(y) == 32:
        return y 
    else:
        for i in range(32 - len(y)):
            y = "0" + y
    return y
    

def convert_array_to_binary(y):
    res = ""
    for i in range(32):
        res += str(y[i])
    return res

"""""
def inversion_ligne_7(Y_bar):
    Y_bar = str(Y_bar)
    Y_bar = add_O(Y_bar)
    res = [-1]*32
    size=32 
    # les bits de 20 --> 31
    for i in range(20,32):
        res[i]=int(Y_bar[size-(i+1)])
    # les bits de 8 --> 20
    for i in range (8,20):
        res[i]=int(Y_bar[size-(i+1)]) ^ int(Y_bar[(size-(i+1))-12])
    for i in range (8):
        res[i]=int(Y_bar[size-(i+1)]) ^ res[i+12]
    
    res.reverse()
    res_str = convert_array_to_binary(res)
    return int(res_str,10)
 """


def inversion_ligne_7(Y_bar):
    Y_bar = str(Y_bar)
    Y_bar = add_O(Y_bar)
    Y_bar=Y_bar[::-1]  
    res = [-1]*32
    size=32 
    # les bits de 20 --> 31
    for i in range(21,32):
        res[i]=int(Y_bar[i])
    # les bits de 8 --> 20
    for i in range (10,21):
        res[i]=int(Y_bar[i]) ^ int(Y_bar[i+11])
    for i in range (10):
        res[i]=int(Y_bar[i]) ^ res[i+11]
    
    res.reverse()
    res_str = convert_array_to_binary(res)
    return int(res_str,10)

#b = 10011101001011000101011010000000
def inverse_line_8(y_bar_bin):
    y_bar_bin = str(y_bar_bin)
    y_bar_bin = add_O(y_bar_bin)
    res = [-1] * 32
    size_y = 32

    #0..6, 8, 11, 13, 15..17, 20, 22, 23, 25, 29, 30
    for i in range(7):
        res[i] = int(y_bar_bin[size_y - (i + 1)])
    res[8] = int(y_bar_bin[size_y - 9])
    res[11] = int(y_bar_bin[size_y - 12])
    res[13] = int(y_bar_bin[size_y - 14])
    for i in range(15, 18):
        res[i] = int(y_bar_bin[size_y - (i + 1)])
    res[20] = int(y_bar_bin[size_y - 21])
    for i in range(22, 24):
        res[i] = int(y_bar_bin[size_y - (i + 1)])
    res[25] = int(y_bar_bin[size_y - 26])
    for i in range(29, 31):
        res[i] = int(y_bar_bin[size_y - (i + 1)])

    res[27] =int(y_bar_bin[size_y - 28]) ^ res[20]
    res[24] =int(y_bar_bin[size_y - 25]) ^ res[17]
    res[31] =int(y_bar_bin[size_y - 32]) ^ res[24]
    res[18] =int(y_bar_bin[size_y - 19]) ^ res[11]
    res[12] =int(y_bar_bin[size_y - 13]) ^ res[5]
    res[19] =int(y_bar_bin[size_y - 20]) ^ res[12]
    res[26] =int(y_bar_bin[size_y - 27]) ^ res[19]
    res[10] =int(y_bar_bin[size_y - 11]) ^ res[3]
    res[9] =int(y_bar_bin[size_y - 10])^ res[2]
    res[7] =int(y_bar_bin[size_y - 8]) ^ res[0]
    res[14] =int(y_bar_bin[size_y - 15]) ^ res[7]
    res[21] =int(y_bar_bin[size_y - 22]) ^ res[14]
    res[28] =int(y_bar_bin[size_y - 29]) ^ res[21]

    res.reverse()
    res_str = convert_array_to_binary(res)
    return int(res_str,10)

    

def inverse_line_9(y_bar_bin):
    #c = 11101111110001100000000000000000
    y_bar_bin = str(y_bar_bin)
    y_bar_bin = add_O(y_bar_bin)
    res = [-1] * 32
    size_y = 32
    for i in range(17):
        res[i] = int(y_bar_bin[size_y - (i + 1)])
    for i in range(19, 22):
        res[i] = int(y_bar_bin[size_y - (i + 1)])
    res[28] = int(y_bar_bin[size_y - 29])

    #
    for i in range(29, 32):
        res[i] = int(y_bar_bin[size_y - (i + 1)]) ^ res[i - 15]
    for i in range(22, 28):
        res[i] = int(y_bar_bin[size_y - (i + 1)]) ^ res[i - 15]
    for i in range(17, 19):
        res[i] = int(y_bar_bin[size_y - (i + 1)]) ^ res[i - 15]

    res.reverse()
    res_str = convert_array_to_binary(res)
    return int(res_str, 10)

#y = y ^ (y >> 1)
def inverse_line_10(y_bar):
    #on retire le "0b"
    y_bar_bin = convert_binary(y_bar)

    #pour le 32e bit (le bit de poids fort)
    res = [-1] * 31
    res.append(int(y_bar_bin[0]))
    res.reverse()
    for i in range(1, 32):
        res[i] = int(y_bar_bin[i]) ^ res[i - 1]


    res_str = convert_array_to_binary(res)
    return int(res_str, 10)


def test_line_7(y):
    return  y ^ (y >> 11)

def test_line_8(y):
    global s, b
    return y ^ ((y << s) & b)

def test_line_9(y):
    global c, t
    return y ^ ((y << t) & c)

def test_line_10(y):
    return  y ^ (y >> 1)



y1 = 3785821843

y2= test_line_7(y1)
y3 = test_line_8(y2)
y4 = test_line_9(y3)
y5 = test_line_10(y4)

res1 = inverse_line_10(y5)
res2 = inverse_line_9(res1)
res3 = inverse_line_8(res2)
res4 = inversion_ligne_7(res3)

print(res4)
print(bin(y1)[2:])



"""
21--->31 (ok)

b20-> a20 xor a31
.
.
.
b10 -> a10 xor a21 

b9 -> a9 xor a20     a20



"""