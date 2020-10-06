import math
def xor(a, b):
    # a XOR b
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

def encryptBLUM(p, q, a, b, m, x0):
    #encrypt using Blum-Goldwasser
    n=p*q #public key step a based on lecture 8.1 slide 8
    k= int(math.log(n,2)) #k, h and t are found based on step b on lecture 8.1 slide 8
    h= int(math.log(k,2))
    t= int(len(m)/h)
    xi = x0 #seed given
    c = ''
    for i in range(t): #for i from 1 to t
        #this loop is based on step d in lecture 8.1 slide 8
        mi = m[i*h:(i + 1)*h] # get section mi of length t
        xi = (xi ** 2) % n #compute xi as xi-1^2 modn
        xi_bin = bin(xi) #convert to binart string
        pi = xi_bin[-h:] # get first h values of xi
        ci = xor(str(pi), mi) #xor this with m1 to get ciphertext block
        c += ci
    xi = (xi ** 2) % n #step e lecture 8.1 slide 8
    return c, xi #return c and seed xi, step f lecture 8.1 slide 8

def decryptBLUM(p, q, a, b, x1, c):
    #decrypt using Blum-Goldwasser
    #get general info
    n = p * q
    k= int(math.log(n,2))
    h= int(math.log(k,2))
    t = int(len(c) / h)

    d1 = int((((p + 1) / 4)**(t + 1)) % (p - 1)) # step a lecture 8.1 slide 9
    d2 = int((((q + 1) / 4)**(t + 1)) % (q - 1)) # step b lecture 8.1 slide 9
    u = (x1**d1) % p # step c lecture 8.1 slide 9
    v = (x1**d2) % q # step d lecture 8.1 slide 9

    x0 = (v*a*p + u*b*q) % n # step e lecture 8.1 slide 9

    xi = x0
    m = ''
    for i in range(t): #from 1 to t do this
        #this loop is step f lecture 8.1 slide 8
        ci = c[i*h:(i + 1)*h] #get h length section of c
        xi = (xi**2) % n #compute xi as xi-1^2 modn
        xi_bin = bin(xi) #convert to binary string
        pi = xi_bin[-h:] #get first h values of xi
        mi = xor(str(pi), ci) #xor this with m1 to get plaintext block
        m += mi
    return m
# starting values
p= 499
q= 547
m= 'NETSEC' #message
mb= '010011100100010101010100010100110100010101000011' #message in binary
x0= 159201 #seed
a=-57 #found a and b values using euclid
b=52
cipher= encryptBLUM(p,q,a,b,mb,x0)
#print("Ciphertext:", cipher)
plain= decryptBLUM(p, q, a, b, cipher[1], cipher[0])
#print("Decrypted Plaintext:", plain)
