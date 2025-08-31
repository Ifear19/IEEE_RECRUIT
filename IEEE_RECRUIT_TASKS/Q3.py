#Q3 NUMPY ARRAYS 

import numpy as np
matrix=np.random.randint(1,101,size=(5,5))#considering 1 and 100 to be inclusive

print("5x5 matrix")
print(" ")
print(matrix)

print("maximum value:",np.max(matrix))
print("minimum value:",np.min(matrix))
print("mean value:",np.mean(matrix))

normalised=((matrix-np.min(matrix))/(np.max(matrix)-np.min(matrix)))
print("\nnormalised matrix\n" ,normalised.round(2) ) #used the round fun to make the matrix look more clean

flat_sort=np.sort(matrix.flatten())#this will first flatten the matrix and then sort it

print("\nflattened and sorted array\n",flat_sort)#using \n sequence to get ouput in other line


