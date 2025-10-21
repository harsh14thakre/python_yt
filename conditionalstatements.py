#--------------------------------------------If else----------------------------------------------

# a = 13

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")
#ANS= I will do task A    


# money = int(input("Please provide the money ;-"))

# if money == 10:
#     print("I will have a chocobar icecream")

# elif money==20:
#     print("I will have a mango dolly")

# elif money==20:
#     print("I will have a mango dolly")    

# else:
#     print("I will have a mango dolly")


#-------------------------------------If else Questions-----------------------------------------------

# Q1-> Accept two numbers and print the greatest between them

# num1 = int(input("Enter the first number"))
# num2 = int(input("Enter the second number"))

# if num1 > num2:
#     print(f'{num1} is greater')

# else if:
#     print(f'{num2} is greater')

# else:
#     print("Both the numbers are same")    

#--------------------------------------------------------------------------------------------------

# Q2-> Accept the Gender from the user as char and print respective greeting message.

# gender = input("Enter your gender as characters (M or F):-")

# if gender=='M' or gender=='m':
#     print("Namaste sir")

# elif gender=='F' or gender=='f':
#     print("Namaste Maam")    

# else:
#     print("Unidentified gender")

#--------------------------------------------------------------------------------------------------

# Q3-> Accept an integer and check whether it is an even number or odd.

# num = int(input("Enter the number"))

# if num%2==0:
#     print("This is even number")

# else:
#     print("This is odd number")

#---------------------------------------------------------------------------------------------------

# Q4-> Accept name and age from the user. Check if the user is a valid voter or not.

# name= input("Please enter your name\n")
# age=int(input("Please enter your age\n"))

# if age>=18:
#     print(f'Hello {name} you are a valid voter')

# else:
#     print(f'Hello {name} you are not valid for voting but you can vote after {18-age} years ')
     
#----------------------------------------------------------------------------------------------------

# Q5-> Accept a year and check if it a leap year or not (google to find out what is a leap year).

# year = int(input("Enter your year\n"))

# if year%100==0 and year%400==0:
#     print("This is a leap year")

# elif year%100!=0 and year%4==0:
#     print("Its a leap year")    

# else:
#     print("This is not a leap year")


# Q6-> If-elif ladder

temp=int(input("Enter temperature in degree celsius\n"))

if temp<0:
    print("Freezing cold")

elif temp>=0 and temp<=10:
    print("Very cold")

elif temp>=10 and temp<=20:
    print("Cold")

elif temp>=20 and temp<=30:
    print("Pleasant")

elif temp>=30 and temp<=40:
    print("Hot")

else:
    print("Very hot")

