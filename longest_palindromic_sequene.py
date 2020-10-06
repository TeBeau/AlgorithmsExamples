import random
def palindrome(s):
    n= len(s)
    #create table
    A= [[0 for x in range(n)]for x in range(n)]
    #strings of len 1 are palindromes of len 1
    for i in range(n):
        A[i][i]=1
    #Fill table
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            if s[i]==s[j] and l==2:
                A[i][j]=2
            elif s[i]==s[j]:
                A[i][j]= A[i+1][j-1]+2
            else:
                A[i][j]= max(A[i][j-1], A[i+1][j])
    return A[0][n-1]

s= [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
print("small palindrome len is... ", palindrome(s))

long= [random.randrange(1, 100, 1) for n in range(1000)]
print("long palindrome len is... ", palindrome(long))
#turns out this is typically 170-180