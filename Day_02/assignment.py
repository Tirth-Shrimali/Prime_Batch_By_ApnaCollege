'''
    1.Write a program that asks the user for their name and age, then prints a sentence like : 
    Hello Shradha, you are 21 years old! 
'''



# name = input("Enter your name : = ")
# age = int(input("Enter your age : = "))
# print("Hello",name,",you are ",age,"years old!")



'''
    2.Take 2 numbers as input from the user and prints their sum, difference, product, and quotient.
'''



# num1 = int(input("\nEnter the first number"))
# num2 = int(input("Enter the second number"))
# print("\nSum of",num1,"&",num2,"is : = ",num1+num2)
# print("Difference of",num1,"&",num2,"is : = ",num1-num2)
# print("Product of",num1,"&",num2,"is : = ",num1*num2)
# print("Quotient of",num1,"&",num2,"is : = ",num1//num2)



'''
    3.Ask the user to enter 2 integers and 1 float. Convert them all to floats and print their average
'''



# a = float(input("Enter first integer: "))
# b = float(input("Enter second integer: "))
# c = float(input("Enter a float: "))

# avg = (a + b + c) / 3

# print("Average =", avg)



'''
    4.The user enters a string containing a number (e.g., "45").Convert it to 
        an integer
        a float
        a string again
    print all three values with thaier types
'''



# n = input("Enter a number: ")

# a = int(n)
# b = float(n)
# c = str(n)

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))



'''
    Q5. Evaluate and print the result of the following expression: 
    x = 10 + 3 * 2 ** 2 
    Based on what you learnt in the lecture explain why the output is what it is.
'''



# x = 10 + 3 * 2 ** 2
# print(x)



'''
    Q6. Write a program to swap values of two numbers entered by the user. 
'''



# a = input("Enter first number: ")
# b = input("Enter second number: ")

# a, b = b, a

# print("First =", a)
# print("Second =", b)



'''
    Q7. Ask the user for a temperature in Celsius (string input). Convert it to , 
    then calculate and print temperature in Fahrenheit. 
    float 
    Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 
    32 
'''



# c = float(input("Enter temperature in Celsius: "))

# f = (c * 9 / 5) + 32

# print("Fahrenheit =", f)



'''
    Q8. Take the radius (r) as user input and print the area. 
    Area = π * r2 
    Use the formula: 
    (value of π = 3.14)
'''



# r = float(input("Enter radius: "))

# area = 3.14 * r * r

# print("Area =", area)



'''
    Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
    compute simple interest: 
        SI = (P ∗ R ∗ T )/100
'''



# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# si = (p * r * t) / 100

# print("Simple Interest =", si)



'''
    Q10. Take a decimal number as input (like 45.78) and output its: 
     
    • integer part - 
    45 
    • fractional part - 
    .78
'''



# n = float(input("Enter a decimal number: "))

# integer = int(n)
# fraction = n - integer

# print("Integer Part =", integer)
# print("Fractional Part =", fraction)