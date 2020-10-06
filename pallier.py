import random

def L(x):
    #l(x) equation used in decryption shown in lecture 9.2
    n= 293*433
    l=((x-1)%(n**2))/n
    return l

def encrypt(m):
    n= 293*433 #p*q
    g= 6497955158
    r= [35145, 74384, 10966, 17953, 7292]
    u= r[m-1]
    #next three lines are the encryption as shown in lecture 9.2
    cipher= (g**m)
    cipher= cipher*(u**n)
    cipher= cipher%(n**2)
    return cipher

def decrypt(c):
    n= 293*433 #p*q
    l= 31536 #lambda
    m=((L((c**l)%(n**2)))*53022)%n #decryption as shown in lecture 9.2
    return m

m=1
#cryptocounter from 1 to 5
while m <= 5:
    c= encrypt(m)
    print("m =", m)
    print("c =", c)
    m=m+1
