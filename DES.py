#Simplified DES encryption
def permute(s, a, n):
    #function to permutate string s using array a, n is the length of the string
    p = ""
    for i in range(0, n):
        p= p + s[a[i] - 1]
    return p

def shift_left(string, shifts):
    #shifts values of the string left by that amount
    s = ""
    for i in range(shifts):
        for j in range(1,len(string)):
            s = s + string[j]
        s = s + string[0]
        string = s
        s = ""
    return string

def xor(a, b):
    # a XOR b
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

def tobin(i):
    #translates the s-box values to binary
    if i == 3: return "11"
    elif i == 2: return "10"
    elif i == 1: return "01"
    else: return "00"

def F(string, key):
    # The F funtion

    #permute and expand input string
    p1= permute(string, [4, 1, 2, 3], len(string))
    p2= permute(string, [2, 3, 4, 1], len(string))
    bit8=p1+p2
    #xor this with the given key
    bit8= xor(bit8, key)
    #split the value into two pieces  and use those to fetch the s-box value
    s1= bit8[0:4]
    s2= bit8[4:8]
    t0= [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    t1= [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    i1= int(s1[1])*2 + int(s1[2]) #2nd and 3rd value of the 1st half of the string into ints
    i2= int(s1[0])*2 + int(s1[3]) #1st and 4th value of the 1st half of the string into ints
    new1= t0[i1][i2] #fetching from s-box
    new1= tobin(new1)#returning to binary string
    i3= int(s2[1])*2 + int(s2[2]) #same as above with 2nd string
    i4= int(s2[0])*2 + int(s2[3])
    new2= t1[i3][i4]
    new2= tobin(new2)
    new= new1+new2 #new string is the combination of these 2 string fragments
    return permute(new, [2, 4, 3, 1], len(new)) #return permuted version of string

def get_keys(key):
    #get key 1 and key 2 from original key
    key= permute(key, [3, 5, 2, 7, 4, 10, 1, 9, 8, 6], len(key)) #initial permutation
    #split key in  half
    p1= key[0:6]
    p2= key[6:10]
    #1st shift left
    p1= shift_left(p1, 1)
    p2= shift_left(p2, 1)
    #add these together and permute to get key 1
    p= p1+p2
    k1= permute(p, [6, 3, 7, 4, 8, 5, 10, 9], 8)
    # same as above but with 2 shifts (according to TA on gradescope)
    p1= shift_left(p1, 2)
    p2= shift_left(p2, 2)
    p= p1+p2
    k2= permute(p, [6, 3, 7, 4, 8, 5, 10, 9], 8)
    return [k1, k2] #return both keys

def encrypt(plain, key):
    #encryption function
    plain= permute(plain, [2, 6, 3, 1, 4, 8, 5, 7], 8) #initial permutation
    #split text
    p1= plain[0:4]
    p2= plain[4:8]
    #get keys for encryption based on key given
    keys= get_keys(key)
    #xor each half with the F function called on the other
    p1= xor(p1, F(p2, keys[0]))
    p2= xor(p2, F(p1, keys[1]))
    p= p2+p1 #add text fragments together
    return permute(p, [4, 1, 3, 5, 7, 2, 8, 6], 8) #permute and return encrypted text

def decrypt(cipher, key):
    #decryption function
    #same as encryption, adding fragments in reverse order
    cipher= permute(cipher, [2, 6, 3, 1, 4, 8, 5, 7], 8)
    c1= cipher[0:4]
    c2= cipher[4:8]
    keys= get_keys(key)
    c1= xor(c1, F(c2, keys[1]))
    c2= xor(c2, F(c1, keys[0]))
    c= c2+c1
    return permute(c, [4, 1, 3, 5, 7, 2, 8, 6], 8)
