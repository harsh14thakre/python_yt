

# class Factory:
#     a=12 #attribute

#     def hello(self):  #method
#         print("How are you")

#     print("Hello how are you i am getting initialized")

# print(Factory().a)

# Factory().hello()

#-------------------------------------------OBJECTS----------------------------------------------------

# class Factory:
#     a = 12

#     def hello(self):
#         print("How are you")

# obj = Factory()
# obj.hello()
# print(obj.a)        

#----------------------------------------CONSTRUCTOR---------------------------------------------------

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
 
#     def show(self):
#         print(f"Your object details are {self.material},{self.pockets},{self.zips}")

# rebook = Factory("leather",3,2)
# campus = Factory("nylon",3,3)
# rebook.show()
# campus.show()

# print(rebook.pockets)

#------------------------------------------Attributes------------------------------------------------

# -> Attributes are just variable defined under the class

# types of attribute:-
# 1-> Class attribute
# 2-> Instance attribute

#  Types of method:-
# 1-> instance method
# 2-> Class method

# class Animal:
#     name = "Lion"  #class attribute

#     def __init__(self,age):
#         self.age = age   #instance attribute

#     def show(self):   #Instanca method
#         print(f"How are you your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("How are you brother")

#     @staticmethod
#     def static():
#         print("How are you")

# obj = Animal(12)
# obj.show()
# obj.hello()


#--------------------------------------------INHERITANCE-----------------------------------------------

# class Factorymumbai:   # Parent class / superclass
#     a = "I am an attribute mentioned inside factory"
#     def hello(self):
#         print("Hello I am a method mentioned in Factory")

# class Factorypune(Factorymumbai):   #child class
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# obj2.hello()

#------------------------------------------------------------------------------------------------------



