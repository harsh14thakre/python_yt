#--------------------------Inbuild data structures in python-----------------------------------------
#=> There are 4 inbuild data structures in python
#=>List
#=>Tuple
#=>Dictionary
#=>Set

# -------------------------CUSTOM DATA STRUCTURES------------------------------------------------
#=> Stack,Queue,Linked List,Graph etc.

#------------------------------------------------------------------------------------------------

#-----------------------------------LIST-----------------------------------------------

# Mutable
# Duplicates
# Ordered-you can access elements by there locations.
# Heterogenious

#Indexing is allowed
#Slicing is allowed

# l=[1,2,3,4,5.2,6.3,True,print()]
# print(l[0:5]) 

#-------------------------------------------------------------------------------------------------

# l=[1,2,3,4,5.2,6.3]

# for i in range(len(l)):
#     print(l[i]) 

#2nd way directly on values

# for i in l:
#     print(i)

# methods in list:
# append
# insert
# extend
#remove

# l.append(55)
# l.append(66)
# print(l)

#---------------------------------------------------------------------------------------------------

# l=[1,3,4,5]
# l.insert(1,2)
# l.extend([6,7,8])
# print(l)

# l=[1,2,3,2,4,5]
# l.remove(2)            
#First occurence of 2 will be remove

#---------------------------------------------------------------------------------------------------

#----------------------SOME QUESTIONS ON A LIST-----------------------------------------------------

#-> Print positive and negative elements on a list.

# l=[-45,21,-5,98,-56]

# print("Positive elements are:-")
# for i in l:
#     if i>=0:
#         print(i)
# print("Negative elements are:-") 

# for i in l:
#     if i<0:
#         print(i)

#-> Mean of List elements.

# l=[1,2,3,4,5,6,7,8,9]

# sum = 0

# for i in l:
#     sum=sum+i
# print(sum/len(l))    
 
#-----------------------------------------------------------------------------------------------

#-> Find the greatest element and print its index too.

# l=[2,1,3,4,5,66,97,2]
# largest=l[0]
# index=0

# for i in range(len(l)):
#     if largest<l[i]:
#         largest=l[i]
#         index=i
# print(f'The largest element is {largest} with index number {index}')        


# -----------------------------------------------------------------------------------------------

# -> Find the second largest number

# l=[12,54,2,6,8,9,4,74,5,1]

# largest=l[0]
# sec_largest=l[0]

# for i in l:
#     if i>largest:
#         sec_largest=largest
#         largest=i
#     elif i>sec_largest:
#         sec_largest=i

# print(sec_largest,largest)            

#--------------------------------------------------------------------------------------------------

#-> Check if list is sorted or not.

# a=[12,54,2,6,8,9,4,74,5,1]

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted") 

