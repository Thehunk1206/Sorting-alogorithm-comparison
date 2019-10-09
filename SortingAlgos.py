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

#Insertion sort
def InsertionSort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i-1
        while j>=0 and temp < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = temp

#bubble sort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 


#selection sort
def selectionSort(arr):
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j     
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

Functions = [MergeSort,InsertionSort,bubbleSort,selectionSort]