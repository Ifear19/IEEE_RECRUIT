#Q7 INTERSECTION OF TWO ARRAYS

list1=[3, 4, 5, 1, 4, 6, 1, 7, 7]
list2=[5, 8, 2, 9, 9, 4, 6, 3]
intersect=[]
for num in list1:
    if num in list2 and num not in intersect: #this will prevent the repetition of numbers
        intersect.append(num)
if len(intersect)==0:
    print("THERE ARE NO COMMON NUMBERS")
else:
    print("\nlist of common numbers is \n",intersect)  



