import os
os.system('cls')



'''
    5.2     Classes & Objects
'''



# class Student:
#     subject = "python"
#     college = "Abc"
#     year = "4Th year"
# student1 = Student()
# student2 = Student()

# print(Student)      #   shows class type
# print(student1)     #   Memory address for this perticular class
# print(student2)     #   Memory address for this perticular class

# print(student1.subject, student1.college, student1.year)
# print(student2.subject, student2.college, student2.year)

'''
    5.3     Attributes & Methods
'''



'''
    5.4     Constructor - __init__() Method        init - to initialize our object, create an obbject, call automatically
'''


# class Student:
#     def __init__(self):
#         print("Constructor was called...")

# student1 = Student()
# student2 = Student()
# student3 = Student()


# class Student:
#     def __init__(self):
#         print("Constructor was called...")

#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa

# student1 = Student("Tirth", 8.0)
# student2 = Student("Priya", 8.1)
# student3 = Student("Urvashi", 8.4)

# print(student1.name, student1.cgpa)
# print(student2.name, student2.cgpa)
# print(student3.name, student3.cgpa)



'''
    5.5     Types of Constructor
            1.  Default :   =   which init method has only 1 parameter self this is called ...
            2.  Parameterized   :   =   which constructor have more parameter along with self this is called ...

            In python multiple constructor are  not allowed [java and cpp allowed].
                Last constructor are run by default
'''



# class Student:
#     def __init__(self):     #   Default
#         print("Object is being constructed")

#     def __init__(self, name, cgpa): #   Parameterised
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa

# student1 = Student("Rahul",9.1)
# student2 = Student("Tirth",9.3)
# student3 = Student("Shradha",9.2)


# print(student1.get_cgpa())
# print(student2.get_cgpa())
# print(student3.get_cgpa())



'''
    5.6     Attributes - class & instance
            class   :   =   belongs to class, common, create class beacouse it's common 

            instance    :   =   belongs to object, unique, create instance beacouse it's unique
                higher priority [ if both attributes are same name then valid is instance ]
'''



# class Student:
#     collegeName = "ABC college" #   class attributes   ,common      ,fixed for all   ,reduces memory
#     pi = 3.1

#     def __init__(self, name, cgpa):
#         self.name = name    #   instance attributes
#         self.cgpa = cgpa    #   instance attributes
#         self.pi = 3.14

# student1 = Student("Tirth", 9.2)


# print(student1.name)
# print(student1.collegeName)
# # print(Student.name) #   this gives error 'cause in printing instance use object name not class name

# # Print the class with both [class name and ibject name]
# print(Student.collegeName)
# print(student1.collegeName)

# print(Student.pi)
# print(student1.pi)


'''
    5.7     Types of methods    :   =   
        1.Instance Method   :   =
            1. 1st parameter is self
            2. access the class of instance
'''



# class Laptop:
#     storageType = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#     def get_info(self): #   instance method
#         print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storageType}")

# l1 = Laptop("16gb", "512gb")
# l2 = Laptop("8gb", "256gb")

# l1.get_info()
# l2.get_info()



'''
    5.8     class method
        1. 1st parameter is cls
        2. access class attributes, but not instance attributes
        3. decorator @classmethod
'''



# class Laptop:
#     storageType = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#     @classmethod        #   classmethod change the function behaviour from to classmethod
#     def getStorageType(cls):
#         print(f"storage type : = {cls.storageType}")

#     def get_info(self): #   instance method
#         print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storageType}")

# l1 = Laptop("16gb", "512gb")
# l2 = Laptop("8gb", "256gb")

# l1.get_info()
# l2.get_info()

# l1.getStorageType()
# l2.getStorageType()

# # print work in both class name and object name
# print(Laptop.getStorageType)        #   prints the storage type of the laptop's storage type 
# print(l1.getStorageType)        #   prints the storage type of the laptop's storage type 



'''
        5.9     Static Method
                    used when we don't wamt the insatnce or class method 
                    1. 
                        1. compulsory parameter not there
                        2. self parameter not there
                    2. can't access instance and class attributes
                    3. @staticmethod    =   decorator
'''



# class Laptop:
#     storageType = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#     @classmethod        #   classmethod change the function behaviour from to classmethod
#     def getStorageType(cls):
#         print(f"storage type : = {cls.storageType}")

#     def get_info(self): #   instance method
#         print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storageType}")

#     @staticmethod
#     def calcDiscount(price, discount):
#         finalPrice = price - (discount * price /100)
#         print(f"Discounted Price : = {finalPrice}")

# l1 = Laptop("16gb", "512gb")
# l2 = Laptop("8gb", "256gb")
# l1.calcDiscount(40000,10)



'''
    5.10    Practice Problem
                Product Store
                    Design & create an online store for Products (name, price)
                    Track total products being created.
                    Create a soecifc method to calculate discount on each product based on a % parameter. 
'''



# class Product():
#     count = 0   #   class attributes

#     def __init__(self, name, price):
#         self.name = name        #   instance attributes
#         self.price = price      #   instance attributes
#         Product.count += 1

#     def getInfo(self):  #   instance method
#         print(f"Price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def getCount(cls):
#         print(f"total product in store : = (cls.count)")

#     @staticmethod
#     def calculateDiscount(price, percentage):
#         print(f"Discount is : = {price - (price * percentage / 100)}")

# product1 = Product("iPhone",150000)
# product1 = Product("Television",15000)
# product1 = Product("Pen",15)

# product1.calculateDiscount(100,25)



'''
    5.11    Encapsulation   :   =   Capsule of data and method,     Wrapping data & function into -single unit
                also done data hiding
                        1. public data  :   =   access inside and outside class 
                        2. protected    :   =   access in class as well as subclass
                        3. private  :   =   inside the class, not outside the class     [ for outside getter and setter mathod ]

            accountBalance  =   public
           _accountBalance  =   protected
          __accountBalance  =   private

'''



# class BankAccount():
#     def __init__(self, name , accountBalance):
#         self.name = name
#         self.__accountBalance = accountBalance   #   Protected
    
#     def getBalance(self):       #   getter
#         return self.__accountBalance
    
#     def setBalance(self,newBalance):       #   setter
#         self.__accountBalance = newBalance

# Ba1 = BankAccount("Tirth Shrimali", 100001)

# print(Ba1.name,Ba1.getBalance())    #   getter

# Ba1.setBalance(200001)
# print(Ba1.name,Ba1.getBalance())    #   setter

# print(Ba1.name,Ba1._BankAccount__accountBalance)     # Access attribute private outside the calss



'''
    5.12    Inheritance :   =   Use 1 class's property  in another class's property,    Reusing attributes and methods from a parent (base) class.
                                    parent class    ->  child class
                                attributes
                                    access by subclass and also private   :   =   protected
                                    not acces by subclass and also private   :   =   private
'''



# class Employee():
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self,new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject 

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# t1 = Teacher("math")
# print(t1.subject,t1.start_time,t1.end_time)
# t1.change_time("4PM")   #   change time
# print(t1.subject,t1.start_time,t1.end_time)

# staff1 = AdminStaff("Manager")
# print(staff1.role, staff1.start_time, staff1.end_time)



'''
    5.13    Types of Inheritance    :   =   
                    1. Single level Inheritance :   =   employee    ->  Teacher     , only parent and child
                    2. Multi level Inheritance  :   =   employee    ->  adminstaff  ->  account_department     , only parent and child
                    3. Multiple level Inheritance   :   =   employee    ->  adminstaff  ->  account_department     , only parent and child
'''


# class Employee():
#     start_time = "10am"
#     end_time = "6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Account(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary

# acc1 = Account(25000, "CA") 
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


'''Multiple level inheritance'''


# class Teacher():
#     def __init__(self, salary):
#         self.salary = salary
    
# class Student():
#     def __init__(self, cgpa):
#         self.cgpa = cgpa
    
# class TS(Teacher, Student):
#     def __init__(self, salary, cgpa, name):
#         super().__init__(salary)
#         Student.__init__(self, cgpa)
#         self.name = name

# TS1 = TS(15000, 9.3, "Tirth")

# print(TS1.name,TS1.cgpa,TS1.salary)



'''
    5.14    Abstraction :   =   part of abc module in python,     Hiding internal details & showing only essential featuring
                abstract class are blueprint of other classes

                    data hiding is only focused on hiding the data 
                    and 
                    abstraction is focused on which is the hiding the data as well as which is the showing the data  [kyu hide krvu and kyu dekhadvu ]
'''



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound():
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar !!!")

# lion = Lion()
# lion.make_sound()



'''
    5.15    Polymorphism ( Function Overriding )    :   =   direct means Many forms , multiple function with same names
                    1.  Function overriding :   =   done only where inheritance involved.
                                one function already existing in parent class and user redefining the same fucntion in child class so ...  
                    2.  Duck Typing
            poly = many
            morph = forms
'''



# class Employee():
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# e1 = Employee()
# e1.get_designation()



'''
    5.16    Polymorphism    ( Duck Typing ) :   =   walks like a duck and quacks like a duck so we call or treat it like a duck ...
                    2 classes exists no relation or inheritance between them but we need function that done the same work and needs in both classes then ...
'''




class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()
a1 = Accountant()
a1.get_designation()