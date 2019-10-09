import time
import random

NUMBER_OF_ELEMENT = 10000


a = [random.randrange(1,100) for i in range(NUMBER_OF_ELEMENT)]

#Insertion sort
def InsertionSort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i-1
        while j>=0 and temp < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = temp


start = time.time()
InsertionSort(a)
end = time.time()

print("total time taken for sorting by Insertion sort",end - start,"on",NUMBER_OF_ELEMENT,"Elements")


del a