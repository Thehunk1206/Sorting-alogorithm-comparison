from time import time
from random import randrange

import SortingAlgos as SA

import matplotlib.pyplot as plt

fig = plt.figure()
graph1 = fig.add_subplot(1,1,1)
plt.xlabel("Number of Elements")
plt.ylabel("TIme in Sec.")


NUMBER_OF_ELEMENT = [500,1000,5000,10000,50000]
Legends=['MergeSort','InsertionSort','BubbleSort','SelectionSort']
TIME_TAKEN = [[],[],[],[]]

for f in range(len(SA.Functions)):
    for i in NUMBER_OF_ELEMENT:
        a = [randrange(1,100) for i in range(i)]
        start_time = time()
        SA.Functions[f](a)
        end_time = time()
        time_taken = end_time - start_time
        print("time taken for sorting by ",str(SA.Functions[f]),"for",i,"Elements is",time_taken)
        TIME_TAKEN[f].append(time_taken)
        del a
for i in range(len(TIME_TAKEN)):
    print(TIME_TAKEN[i])


for i in range(len(TIME_TAKEN)):
    graph1.plot(NUMBER_OF_ELEMENT,TIME_TAKEN[i])

plt.legend(Legends)
plt.show()

