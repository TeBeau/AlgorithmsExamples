import random 
import math
import time

def selection(A, k):
    i=random.randrange(0, len(A), 1)
    v=A[i]
    AL=[]
    AR=[]
    AV=[]
    for x in A:
        if x>v:
            AR.append(x)
        elif x<v:
            AL.append(x)
        else:
            AV.append(x)
    if len(A)==1:
        return A[0]
    else:
        if k <= len(AL):
            return selection(AL, k)
        elif k > (len(AL)+len(AV)):
            return selection(AR, k-len(AL)-len(AV))
        else:
            return AV[0]


A= [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
k= 10
a= selection(A, k)
print("Answer for small test is", a)

long= [random.randrange(0, (10**7)/100, 1) for n in range(10**7)]
start= time.time()
b= selection(long, (10**7)/2)
end= time.time()
print("Answer for large test is", b)
print("time was... ", end-start)

