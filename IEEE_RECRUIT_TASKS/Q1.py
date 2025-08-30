#Q1 STAR PATTERN

n=int(input('Enter a Number for the star pattern '))
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)#by using this statement I don't need an inner loop