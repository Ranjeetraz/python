## Python Exception Handling – Complete Guide with Examples
# Exception handling allows us to handle runtime errors gracefully, preventing program crashes.

# ------------------------------------------
## 1️⃣ Errors vs Exceptions
# Definition: Errors occur due to syntax issues, while exceptions occur during execution and can be handled.

# SyntaxError (Example of an Error)
# print("Hello"  # Missing closing parenthesis - This will raise a SyntaxError

# Exception Example
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ------------------------------------------
## 2️⃣ try, except, finally Blocks
# Definition: The try block contains the code that may raise an exception. The except block handles the exception, and the finally block always executes.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution complete.")

# ------------------------------------------
## 3️⃣ Catching Multiple Exceptions
# Definition: We can handle multiple exceptions using multiple except blocks or a single except block.
try:
    value = int("abc")  # This will raise a ValueError
except (ValueError, TypeError):
    print("A ValueError or TypeError occurred!")

# ------------------------------------------
## 4️⃣ Raising Exceptions (raise)
# Definition: The raise keyword is used to generate custom exceptions.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    else:
        print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print("Error:", e)

# ------------------------------------------
## 5️⃣ Custom Exceptions
# Definition: We can create our own exceptions by subclassing the Exception class.
class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number!")
    return num ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

# ------------------------------------------
## 6️⃣ Using assert for Debugging
# Definition: The assert statement is used to test conditions. If the condition is False, it raises an AssertionError.
def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print("AssertionError:", e)

# ------------------------------------------
## 7️⃣ Exception Handling with else Block
# Definition: The else block runs only if no exception occurs in the try block.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("You entered a valid number:", num)

# ------------------------------------------
## 8️⃣ Nested try-except Blocks
# Definition: We can use nested try-except blocks to handle different levels of exceptions.
try:
    try:
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
    except IndexError:
        print("Inner Exception: Index out of range!")
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Outer Exception: Cannot divide by zero!")

# ------------------------------------------
## 9️⃣ Logging Exceptions
# Definition: The logging module helps in recording exceptions instead of printing them.
import logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)
try:
    1 / 0  # This will raise ZeroDivisionError
except Exception as e:
    logging.error("Exception occurred: %s", e)
    print("An error occurred, check the log file.")

# ------------------------------------------
## 🔟 Handling SystemExit Exception
# Definition: The SystemExit exception is raised when sys.exit() is called.
import sys
try:
    sys.exit("Exiting the program!")
except SystemExit as e:
    print("Caught SystemExit exception:", e)
