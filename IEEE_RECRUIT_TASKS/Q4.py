#Q4 SLICING

import numpy as np
matrix=np.random.randint(1,101,size=(5,5))
sliced=matrix[1:4,1:4]#indexing starts from 0 and last number in slicing is not included
print("\n sliced matrix\n",sliced)
row=sliced[0,:]#taking the first row
col=sliced[:,-1]#taking the last col by negative indexing(-1 for last elememt,-2 for second last and so on)

print("\n DOT PRODUCT\n",np.dot(row,col))

