'''
1. Defining Functions:
Write a function greet() that prints "Hello, Python Learner!" when called.
Write a function square(num) that returns the square of a given number. Test it with different numbers.


2. Function Arguments & Return Values:
Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last" .


Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)


3. Lambda Functions:
Write a lambda function that adds two numbers and test it.
Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.


4. Recursion in Python:
Write a recursive function factorial(n) that returns the factorial of a number.
Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.


5. Modules and Pip – Using External Libraries:
Import the math module and use it to:
Find the square root of 144
Calculate sin(90°) (hint: use math.radians() )
Install and import the requests module (if available) and use it to fetch data from "https://api.github.com" .



6. Variable Scope and Docstrings:
Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. 
Observe whether the value persists across function calls.
Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.


7. Bonus Challenges:
Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .
Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

'''





# 1. Defining Functions 
def greet():
    print("Hello, Python Learner!")
greet()

num = int(input("Enter Int num :"))
def square(num):
    return num*num
print(square(num))
print("\n\n\n")




# 2. Function Arguments & Return Values
def full_name(first,last):
    return f"{first} {last}"

print("jubayed","ahmed")

def calculate_area(length,width=10):
    return length*width
print(calculate_area(13,20))
print(calculate_area(13))
print("\n\n\n")



# 3.Lambda Function
sum = lambda a,b: a+b 
print(sum(5,2))



List1 = [1,2,3,4,5]
print(list(map(square,List1)))

# 4. Recursion in Python
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) 
    
print(factorial(5))



def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    
print(sum_of_digits(1234))
print("\n\n\n")

'''
7532
2 + sum_of_digits(753)
5 + sum_of_digits(75)
7 + sum_of_digits(7)
'''



# 5. Modules and Pip – Using External Libraries:    
import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))
'''
import requests                                    # Uncomment this line if requests module is installed  # pip install requests
response = requests.get("https://api.github.com")
print(response.status_code)
print("\n\n\n")

'''


# 6. Variable Scope and Docstrings:
counter = 0  # Global variable
def increment():
    global counter  # Access the global variable
    counter += 1
    print(counter)          
increment()
increment()     
increment()
increment()
increment()
increment()
increment()        
increment()
increment() 
print("\n")



def multiply(a,b):
    """This function multiplies two numbers and returns the result."""
    return a*b
print(multiply(5,3))
print(multiply.__doc__)
print("\n\n\n")




# 7. Bonus Challenges:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
fibonacci(10)
print("\n")


def safe_divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return a/b
print(safe_divide(10,2))
print(safe_divide(10,0))
print("\n\n\n")


# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file. (In My_Module.py)
from My_Module import is_even
print(is_even(4))
print(is_even(5))
print("\n\n\n")