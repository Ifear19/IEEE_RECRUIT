#Q1 STAR PATTERN

n=int(input('Enter a Number '))
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)
    

#Q2 PALINDROME WORDS

print('Enter your paragraph(press enter on a blank line to finish)')
lines=[]
while True:
    line=input()
    if line=="":
        break
    lines.append(line)

paragraph=' '.join(lines)
print('your paragraph is ',paragraph)
words=paragraph.split()
if len(words)>100:
    print("Pls check the word limit")
a=0
for word in words:
    w=word.lower()
    if w==w[::-1] and len(w)>=1:
        print(word)
        a=a+1
if a==0:
    print("no palindrome word in para")



#Q3 NUMPY ARRAYS 

import numpy as np
matrix=np.random.randint(1,101,size=(5,5))#considering 1 and 100 to be inclusive
print("5x5 matrix")
print(matrix)

print("maximum:",np.max(matrix))
print("minimum:",np.min(matrix))
print("mean:",np.mean(matrix))

normalised=((matrix-np.min(matrix))/(np.max(matrix)-np.min(matrix)))
print("\nnormalised matrix\n" ,normalised.round(2) )

flat_sort=np.sort(matrix.flatten())
print("\nflattened and sorted matrix\n",flat_sort)



#Q4 SLICING

import numpy as np
matrix=np.random.randint(1,101,size=(5,5))
sliced=matrix[1:4,1:4]#indexing starts from 0 and last number in slicing is not included
print(sliced)
row=sliced[0,:]
col=sliced[:,-1]
print(np.dot(row,col))



#Q7 INTERSECTION OF TWO ARRAYS

list1=[3, 4, 5, 1, 4, 6, 1, 7, 7]
list2=[5, 8, 2, 9, 9, 4, 6, 3]
intersect=[]
for i in list1:
    if i in list2 and i not in intersect:
        intersect.append(i)
print(intersect) 









