import os
os.system("cls")



'''
    3.1     Conditional Statements
'''



# color = input("Enter the color : = ")

# if color == "red":
#     print("STOP!!")
# elif color == "yellow":
#     print("wait")
# elif color == "green":
#     print("GO")
# else:
#     print("Wrong color for traffic lights")



'''
    3.2     Practice Examples
'''



# age = int(input("Enter the number : = "))

# if ( age < 13):
#     print("Child")
# elif (age >= 13 and age < 18):
#     print("Teenager")
# else:
#     print("Adult")



# userName = input("Enter the username : = ")
# password = input("Enter the passwrd : = ")

# if (userName == "admin" and password == "pass"):
#     print("Login Successfully . ")
# elif (userName != "admin"):
#     print("Wrong Username")
# else:
#     print("Wrong password")



# num = int(input("Enter the number"))

# if (num % 5 == 0):
#     print("Yes it's multiplication of 5")
# else:
#     print("No it's not multiplication of 5")



'''
    3.3     Odd or even
'''



# num = int(input("Enter the number"))

# if (num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")



'''
    3.3     Nesting
'''



# userName = input("Enter the username : = ")
# password = input("Enter the passwrd : = ")

# if (userName == "admin" and password == "pass"):
#     print("Login Successfully . ")
# else:
#     if (userName != "admin"):
#         print("Wrong Username")
#     else:
#         print("Wrong password")



'''
    3.4     Match Case
'''



# color = input("Enter the color : = ")

# match color:
#     case "green":
#         print("Go")
#     case "yellow":
#         print("wait")
#     case "red":
#         print("stop")
#     case _:
#         print("Wrong color")



'''
    3.6     Loops using while
'''



# count = 1

# while count <= 10:
#     print(count)
#     count += 1



'''
    3.7     Practice Examples
'''



# count = 1

# while count <= 5:
#     print(count)
#     count += 1


# print("")
# count = 5

# while count >= 1:
#     print(count)
#     count -= 1


'''
    3.8     Multiplication Table of N
'''



# num = int(input("Enter the number : = "))

# i = 1
# while (i <= 10):
#     print(num * i)
#     i += 1



'''
    3.9     Break & Continue
'''



# i = 1

# while (i <= 10):
#     if (i % 6 == 0):
#         break     #
#     print(i)
#     i += 1
# print("Outside loop now ...")



# i = 0

# while (i <= 10):
#     i += 1
#     if (i % 3 == 0):
#         continue      #
#     print(i)
# print("Outside loop now ...")



'''
    3.10        Loops using for loop
'''



# string = "hello"

# for var in string:
#     print(var)


# if 'o' in string:
#     print("exists")


# i = 0
# for i in range(6):
#     print(i)


# word = "artificial intelligence"
# ans = 0 

# for ch in word:
#     if ch == 'i':
#         ans += 1
# print(ans)



'''
    3.11        Vowel Count
'''



# word = "artificial"
# cnt = 0

# for ch in word:
#     if( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' ):
#         cnt += 1
# print(cnt)



'''
    3.12        Range() start stop step
'''



# for i in range(1, 10, 2):
#     print(i)



'''
    3.13      Sum of N numbers
'''



# num = int(input("Enter the choice : = "))

# sum = 0

# for i in range(1, num+1):
#     sum += i
# print(sum)

'''
    3.14        Functions 
'''


# def helloWorld():
#     print("Hello world from tirth")

# helloWorld()


# def sum(a, b):
#     s = a + b 
#     return s

# a = int(input("Enter the number : = "))
# b = int(input("Enter the number : = "))

# ans = sum (a, b)
# print(ans)
# print(sum(a, b))



'''
    3.15        Practice Examples
'''



# def avg(a, b, c):
#     return (a + b + c)/2

# print(avg(2, 4, 6))


# def sum(a, b = 1):
#     return a + b
# print(sum(5))
# print(sum(5, 4))



'''
    3.16        Types of Functions
'''


'''
    3.17        Lambda Functions
'''



# sum = lambda a, b, c : a + b + c 
# print(sum(1, 2, 3))




'''
    3.18        Fcatorial of N
'''



# def calcFactorial(n):
#     fact = 1
    
#     for i in range(1, n+1):
#         fact *= i
    
#     return fact

# n = int(input("Enter the number"))
# print(calcFactorial(n))
