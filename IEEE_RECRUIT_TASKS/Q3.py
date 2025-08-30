#Q3 NUMPY ARRAYS 

import numpy as np
matrix=np.random.randint(1,101,size=(5,5))#considering 1 and 100 to be inclusive

print("5x5 matrix")
print(" ")
print(matrix)

print("maximum:",np.max(matrix))
print("minimum:",np.min(matrix))
print("mean:",np.mean(matrix))

normalised=((matrix-np.min(matrix))/(np.max(matrix)-np.min(matrix)))
print("\nnormalised matrix\n" ,normalised.round(2) )

flat_sort=np.sort(matrix.flatten())
print("\nflattened and sorted array\n",flat_sort)#using \n sequence to get ouput in other line