""" 
    Q1. Write a program that takes as input. Using conditional statements, 
    calculate the final tax rate based on these rules: 
    • If salary < 30,000 → 5% 
    • If salary is 30,000–70,000 → 15% 
    • If salary > 70,000 → 25%
"""



salary = float(input("Enter salary: "))

if salary < 30000:
    tax = salary * 0.05
elif salary <= 70000:
    tax = salary * 0.15
else:
    tax = salary * 0.25

print("Tax =", tax)



"""  
    Q2. Write a function that takes two integers and and prints all even 
    numbers between them (inclusive). 
"""



def even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

even_numbers(x, y)



"""  
     
    Q3. Write a function that prints the digits of a number, . 
    For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them. 
    
    
    [Hint - The right most digit of a number N is N%10. 
    And to remove the right most digit from a number, we can do N = N / 10.] 
"""



def print_digits(n):
    while n > 0:
        print(n % 10)
        n //= 10

num = int(input("Enter a number: "))
print_digits(num)



"""  
    Q4. Write a function to return the count the number of digits in a number
"""



def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("Enter a number: "))
print(count_digits(num))



""" 
    Q5. Write a function to return the sum of digits of a number
"""



def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
print(sum_digits(num))



"""  
    Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 
    and 5.
"""



for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)



""" 
    Q7. Design a program to continuously input a number from user & print if it is 
    positive or negative until the user     enters “Quit”. 
"""



while True:
    value = input("Enter a number or Quit: ")

    if value.lower() == "quit":
        break

    num = int(value)

    if num >= 0:
        print("Positive")
    else:
        print("Negative")



"""
    Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create 
    a function calculator(a, b, operation) that performs addition, subtraction, 
    multiplication, or division based on the operation parameter. 
    [ 
    operation 
    parameter can have values , , & .
"""



def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid Operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation: ")

print(calculator(a, b, op))



"""
Q9 (Full Question)

Write a function that returns True if n is a prime number and False otherwise, using a loop.

Hint:

We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
A non-prime number n will always get divided by at least one number in the range [2, n−1].
Example: For 9, we'll check numbers from 2 to 8. Since 9 is divisible by 3, it is not prime.
Example: For 7, we'll check numbers from 2 to 6. Since it is not divisible by any of them, it is prime.
"""



def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

print(is_prime(num))



""" 
    Q10. Letʼs create a “Number Guessing Game”. Given a secret number (already 
    decided by you), write a program that asks the user to guess it and prints: 
    "Too high" if the guess is above the number 
    "Too low"  if the guess is below 
    "Correct!" if the guess matches
 """



secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break