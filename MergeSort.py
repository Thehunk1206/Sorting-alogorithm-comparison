from time import time
from random import randrange


NUMBER_OF_ELEMENT = 10000


a = [randrange(1,100) for i in range(NUMBER_OF_ELEMENT)]


    
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        R = arr[mid:]
        L = arr[:mid]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    

start_time = time()
MergeSort(a)
end_time = time()


print("time taken",end_time - start_time)

del a
