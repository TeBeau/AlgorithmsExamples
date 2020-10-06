import time
import random

def quick_sort(A, start, end, k):
    if start >= end:
        return A[int(k-1)]
    p = partition(A, start, end)
    return quick_sort(A, start, p-1, k)
    return quick_sort(A, p+1, end, k)

def partition(A, start, end):
    pivot = A[start]
    low = start + 1
    high = end

    while True:
        while low <= high and A[high] >= pivot:
            high = high - 1
        while low <= high and A[low] <= pivot:
            low = low + 1
        if low <= high:
            A[low], A[high] = A[high], A[low]
        else:
            break

    A[start], A[high] = A[high], A[start]

    return high

array =  [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
k= 10
a= quick_sort(array, 0, len(array) - 1, k)
print("The answer for small test is ", a)

long= [random.randrange(0, (10**7)/100, 1) for n in range(10**7)]
start= time.time()
b= quick_sort(long, 0, (10**7)-1, (10**7)/2)
end= time.time()
print("Answer for large test is", b)
print("time was... ", end-start)