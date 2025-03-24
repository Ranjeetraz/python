## Python Functions – Basic to Advanced Examples
# Functions allow us to structure our code efficiently, make it reusable, and improve readability.

# ------------------------------------------
## 1️⃣ Simple Function (Basic Function)
def greet():
    """This function prints a greeting message."""
    print("Hello, Welcome to Python!")

greet()  # Function Call

# ------------------------------------------
## 2️⃣ Function with Parameters(Positional Parameters)
def add(a, b):
    """This function takes two numbers as input and returns their sum."""
    return a + b

print(add(5, 10))  # Output: 15

# ------------------------------------------
## 3️⃣ Function with Default Parameter
def greet(name="Guest"):
    """This function greets the user with a default or provided name."""
    print("Hello,", name)

greet()         # Output: Hello, Guest
greet("Alice")  # Output: Hello, Alice

# ------------------------------------------
## 4️⃣ Function with Multiple Arguments (*args)
def add_numbers(*numbers):
    """This function accepts multiple numbers and returns their sum."""
    return sum(numbers)

print(add_numbers(1, 2, 3, 4, 5))  # Output: 15

# ------------------------------------------
## 5️⃣ Function with Multiple Keyword Arguments (**kwargs)
def student_info(**details):
    """This function takes multiple keyword arguments and prints them as key-value pairs."""
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="John", age=20, course="Python")
# Output:
# name: John
# age: 20
# course: Python

# ------------------------------------------
## 6️⃣ Lambda Function (Anonymous Function)
square = lambda x: x * x  # A one-line function to calculate the square of a number
print(square(5))  # Output: 25

# ------------------------------------------
## 7️⃣ Recursive Function (Factorial Calculation)
def factorial(n):
    """This function calculates the factorial of a given number recursively."""
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# ------------------------------------------
## 8️⃣ map() Function (Higher-Order Function)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))  # Applies lambda function to each element
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# ------------------------------------------
## 9️⃣ filter() Function (Higher-Order Function)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filters out even numbers
print(even_numbers)  # Output: [2, 4, 6]

# ------------------------------------------
## 🔟 Generator Function (yield example)
def count_up_to(n):
    """This function generates numbers from 1 to n using a generator."""
    num = 1
    while num <= n:
        yield num  # Yield returns one value at a time
        num += 1

for value in count_up_to(5):
    print(value)

# ------------------------------------------
## 1️⃣1️⃣ Function Decorator
def decorator(func):
    """This function takes another function as input and enhances its behavior."""
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator  # Applying the decorator to modify the behavior of say_hello function
def say_hello():
    print("Hello!")

say_hello()

# ------------------------------------------
## 1️⃣2️⃣ Nested Function (Inner Function)
def outer():
    """This function contains another function inside it."""
    print("Outer function")

    def inner():
        print("Inner function")

    inner()  # Calling inner function

outer()

# ------------------------------------------
## 1️⃣3️⃣ Function Closure
def outer_function(msg):
    """This function returns an inner function that remembers the given message."""
    def inner_function():
        print(msg)
    return inner_function  # Returning inner function

hello = outer_function("Hello, Python!")
hello()  # Output: Hello, Python!

# ------------------------------------------
## 1️⃣4️⃣ Partial Function using functools.partial
from functools import partial

def power(base, exponent):
    """This function calculates the power of a number."""
    return base ** exponent

square = partial(power, exponent=2)  # Creates a partial function where exponent is always 2
print(square(5))  # Output: 25

# ------------------------------------------
## 1️⃣5️⃣ Global & Local Variables
x = 10  # Global variable

def show():
    x = 5  # Local variable
    print("Local x:", x)  # Output: Local x: 5

show()
print("Global x:", x)  # Output: Global x: 10

# ------------------------------------------
## 1️⃣6️⃣ Importing Modules
import math  # Importing built-in module
print(math.sqrt(16))  # Output: 4.0

# Importing specific function
from math import factorial
print(factorial(5))  # Output: 120

# ------------------------------------------
## 1️⃣7️⃣ Creating and Using Custom Modules
# Creating a module (save this in mymodule.py)
# def greet(name):
#     return f"Hello, {name}!"

# Importing the custom module
# import mymodule
# print(mymodule.greet("Alice"))  # Output: Hello, Alice!

# ------------------------------------------
## 1️⃣8️⃣ Python Standard Library Usage
import datetime
print(datetime.datetime.now())  # Output: Current date and time

# ------------------------------------------
## 1️⃣9️⃣ Docstrings & Annotations
def multiply(a: int, b: int) -> int:
    """This function multiplies two integers and returns the result."""
    return a * b

print(multiply(3, 4))  # Output: 12
