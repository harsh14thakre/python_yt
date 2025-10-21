# FUNCTION- It is a block of reusable code and whenever we want to call it then it will only run.
#------------------------------------------------------------------------------------------------

# def hello():
#     print("This is a hello function so i am doing hello")

# hello()    
#-----------------------------------------------------------------------------------------------

# def sum(a,b):
#     print(f"The sum of your numbers is {a+b} ")

# sum(12,12)
# sum(45,45)    

#=> PARAMETERS- The thing you acceopt is parameter 
#=> ARGUMENT-> The thing you provide to parameters is Argument.
#------------------------------------------------------------------------------------------------

#------------------------------THERE ARE THREE TYPES OF ARGUMENT----------------------------------

#=> Positional argument:-

# def sum(a,b):
#     print(f"The sum of your numbers is {a+b} ")

# sum(12,12)
# sum(45,45)    

#-------------------------------------------------------------------------------------------------

#=> Keyword arguments

# def hello(name,age):
#     print(f'your name is {name} and your age is {age}')

# hello(age=21,name="harsh")    

#-------------------------------------------------------------------------------------------------

#=> Default argument:-

# def sum(a,b=45):
#     print(f'The sum is {a+b}')

# sum(12)    

#------------------------------------------------------------------------------------------------

#=> Check whether the string is palindrom or not.

# def pallindrom(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]

#     if rev==st:
#         print(f"{st} is a Palindrom") 

#     else:
#         print(f"{st} is not a palindrom") 

# pallindrom("NAMAN") 
# pallindrom("CURSOR")             

#-------------------------------------------------------------------------------------------------

#----------------------------------------USE OF RETURN-------------------------------------------

# def hello():
#     return "Hello how are you"

# print(hello())

#-------------------------------------------------------------------------------------------------

