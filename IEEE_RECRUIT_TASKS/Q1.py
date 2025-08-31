#Q1 STAR PATTERN

n=int(input('Enter a Number for the star pattern '))
for i in range(1,n+1): #range fun doesn't include the last value so it will make a star of n lines only
     print(' '*(n-i),'*'*i)#by using this statement I don't need to use nested loop

   

