from random import randrange
from time import time

NUMBER_OF_ELEMENTS = 10000

a = [randrange(1,100) for i in range(NUMBER_OF_ELEMENTS)]

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

start = time()
bubbleSort(a)
end = time()

print("time taken to sort the element",end-start)
del a
