#--------------------------------------------FOR LOOP------------------------------------------------

# a = range(1,21,1)

# for i in a:
#     print(i)

# for i in range(1,21,1):
#     print(i)    

#----------------------For printing numbers in reverse----------------------------------------------

# for i in range(10,0,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

# Lets print a table of 5

# n=int(input("Which table you want to print:-"))
# for i in range(n,(n*10)+1,n):
#     print(i)

#---------------------------------------------------------------------------------------------------

# a="I AM A ROCKSTAR"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# b="I AM A ROCKSTAR"

# for i in b:
#     print(i)

#--------------------------------------------BREAK--------------------------------------------------

# for i in range(1,21):
#     if i==15:
#         break
#     else:
#         print(i)  

#-----------------------------------------CONTINUE-------------------------------------------------


# for i in range(1,21):
#     if i==15:
#         continue
#     print(i)  

#-------------------------------------------------------------------------------------------------

# for i in range(1,21):
#     if i==56:
#         print("Break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")    

#-------------------------------------------------------------------------------------------------

# -> Take a number as input and print its table.

# n=int(input("Enter a number which table you want to print"))

# for i in range(1,11):
#     print(f'{n}*{i}={n*i}')

#------------------------------------------------------------------------------------------------

#-> Sum up to n terms.

# n=int(input("Enter any number\n"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f'Your sum is {sum}')

#------------------------------------------------------------------------------------------------

#-> Factorial of a number.

# n=int(input("Enter any number\n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f'Factorial is {fact}')

#------------------------------------------------------------------------------------------------

#-> Print the sum of all even and odd numbers in a range seperately.

# n=int(input("Enter your number:-\n"))
# even=0
# odd=0

# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i    
# print(f'Sum of all even numbers till {n} is {even}\n Sum of all odd numbers till {n} is {odd}')

#--------------------------------------------------------------------------------------------------

#-> Print all the factors of a number.

# n=int(input("Enter the number:-"))
 
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)    

#-------------------------------------------------------------------------------------------------

#-> Write a program to find a perfect number.

# num=int(input("Enter a number to find is it perfect or not\n"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if sum==num:
#     print("This is a perfect number")    
# else:
#     print("This is not a perfect number ")    

#--------------------------------------------------------------------------------------------------

#-> Write a program to check weather the number is prime or not.

# n=int(input("Check weather the number is prime or not\n"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("This is a prime number")

# else:
#     print("This is not a prime number")            

#---------------------------------------------------------------------------------------------------

#-----------------------String concatination-------------------------------------------------

# a = "ROCKSTAR"
# b = " is Harsh"
# print(a+b)

#--------------------------------------------------------------------------------------------------

#-> Reverse string without using any inbuilt function.
 
# a = "ROCKSTAR"

# for i in range(len(a)-1,-1,-1):
#     print(a[i])

#---------------------------------------------------------------------------------------------------

#-> Check weather the string is palindrom or not.

# a="naman"

# b=""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if b==a:
#     print("Your string is palindrom")

# else:
#     print("Its not a palindrom")        

#---------------------------------------------------------------------------------------------------

#-> Count all letters, digits, and special symbols from a given string.

# a = "sdfsogn12413@#$%^&U"

# char=0
# dig=0
# spchr=0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1

# print(f"Your digits are {dig}\n Your alphabets are {char}\n Your special characters are {spchr}")

#---------------------------------------------------------------------------------------------------



#############################################-WHILE LOOP-############################################

#-> Seperate each number

# a = int(input("Tell your number"))

# while a> 0:
#     print(a % 10)
#     a = a // 10

#--------------------------------------------------------------------------------------------------

#-> Accept a number and print its reverse.

# a = int(input("Enter your number"))

# rev=0

# while a>0:
#     rev = rev * 10 + a % 10
#     a = a //10
# print(rev)    

#---------------------------------------------------------------------------------------------------

#-> Accept a number and check 9if its a palindromic number and its reverse are equal).

# a = int(input("Enter your number"))
# palindrom=a
# rev=0

# while a>0:
#     rev = rev *10 + a%10
#     a=a//10
    
# if rev==palindrom:
#     print("This number is palindrom")
# else:
#     print("This number is not palindrom")     

#----------------------------------------------------------------------------------------------------

#-> Create a random number guessing game with python.

# import random 

# num =  random.randint(1,10)

# tries=0

# while True:
#     guess = int(input("Please guess your number between 1 to 10\n"))
#     if num == guess:
#         tries+=1
#         print(f"You are right you guessed the number in {tries} tries")
#         break

#     elif num<guess:
#         print("Go a little lower")
#         tries+=1

#     elif num>guess:
#         print("Go a little higher")
#         tries+=1

#     else:
#         tries+=1
#         print("Sorry you are wrong")    
           
#-----------------------------------------------------------------------------------------------------

# import random

# num = random.randint(1,100)
# tries=0

# while True:
#     guess=int(input("Please guess your number between 1 to 100"))
    
#     if guess==num:
#         tries+=1
#         print(f'You guessed a right number in {tries} tries')
#         break
    
#     elif guess>num:
#         tries+=1
#         print("Go a little lower")

#     elif guess<num:
#         tries+=1
#         print("Go a little higher")

#     else:
#         tries=+1
#         print("You are wrong")        

#----------------------------------------------------------------------------------------------------

