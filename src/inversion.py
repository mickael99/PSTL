
import mersenne_twister as mt


def conversion_base10(s) :
    s= str(s)
    res =0 
    n = len(s)
    for i in range (n) :
        res+= int( s[i] ) * (2**(n-1-i))
    return res

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

#y = y ^ (y >> l)
def inverse_line_10(y_bar):
    y_bar_bin = convert_binary(y_bar)
    y_bar_bin = str(y_bar_bin)
    res = [-1] * 32
    y_bar_bin=y_bar_bin[::-1]  
     # les bits de 14 --> 31
    for i in range(14,32):
        res[i]=int(y_bar_bin[i])
    # les bits de 0 --> 13
    for i in range (14):
        res[i]=int(y_bar_bin[i]) ^ int(res[i+18])
    res.reverse()
    res_str = convert_array_to_binary(res)
    return int(res_str, 10)
    


def inversion (y) :
    res1 = inverse_line_10(y)
    res2 = inverse_line_9(res1)
    res3 = inverse_line_8(res2)
    res4 = inversion_ligne_7(res3)  
    return(conversion_base10(res4))




