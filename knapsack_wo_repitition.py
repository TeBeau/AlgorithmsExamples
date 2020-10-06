def greedy_knapsack(A, W):
    v=0
    w=0
    i=len(A)-1
    while (v < W and i>=0): 
        x= A[i]
        if(w+(x[0])<W):
           v= v+A[i][1]
           w= w+A[i][0]
        i=i-1
    return v

def DP_knapsack(A, W):
    K= [[0 for x in range(0, len(A))]for x in range(0, W+1)]
    for j in range(1,len(A)):
        for w in range(1,W+1):
            if (A[j][0]> w):
                K[w][j]=K[w][j-1]
            else:
                K[w][j]=max(K[w][j-1], K[w-A[j][0]][j-1]+A[j][1])
    return K[w][len(A)-1]

A=  [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108],[113, 107], [114, 110]]
print("For the Greedy Algo, when W is 100, value is... ", greedy_knapsack(A,100))
print("For the Greedy Algo, when W is 200, value is... ", greedy_knapsack(A,200))
print("For the Greedy Algo, when W is 300, value is... ", greedy_knapsack(A,300))
print("For the DP Algo, when W is 100, value is... ", DP_knapsack(A,100))
print("For the DP Algo, when W is 200, value is... ", DP_knapsack(A,200))
print("For the DP Algo, when W is 300, value is... ", DP_knapsack(A,300))