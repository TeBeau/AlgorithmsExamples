import DES

def mac(m, k):
    #given message and key, create a mac code
    #go through m in 8 bit blocks
    i=0
    j=8
    d= m[i:j]
    #encrypt block
    #IV= 0 so there is no need to xor with IV, answer will be the same
    o= DES.encrypt(d, k)
    while j != len(m):
        i=i+8
        j=j+8
        #xor previosly encrypted block w plaintext
        d= DES.xor(o, m[i:j])
        #encrypt newly xord block
        o= DES.encrypt(d, k)
    return o
def vrfy(m, k, mac1):
    #verify given message
    if mac(m, k) == mac1:
        #if mac from message given equals original mac return 1
        return 1
    else: return 0
