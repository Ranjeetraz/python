# Python If-Else Conditions - All Possible Examples with Explanation

# 1. Simple if statement
# Checks if x is greater than 5 and prints a message if true.
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# 2. if-else statement
# Checks if x is greater than 5; if not, executes the else block.
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")  # Output: x is less than or equal to 5

# 3. if-elif-else statement
# Checks multiple conditions: positive, negative, or zero.
x = 0
if x > 0:
    print("Positive Number")
elif x < 0:
    print("Negative Number")
else:
    print("Zero")  # Output: Zero

# 4. Nested if statement
# Checks a condition inside another condition.
x = 20
if x > 10:
    print("x is greater than 10")  # Output: x is greater than 10
    if x > 15:
        print("x is also greater than 15")  # Output: x is also greater than 15

# 5. Logical Operators
x, y = 10, 20
if x > 5 and y > 15:
    print("Both conditions are True")  # Output: Both conditions are True

if x > 5 or y > 25:
    print("At least one condition is True")  # Output: At least one condition is True

if not (x < 5):
    print("x is not less than 5")  # Output: x is not less than 5

# 6. Membership Operators
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")  # Output: Banana is in the list

if "mango" not in fruits:
    print("Mango is not in the list")  # Output: Mango is not in the list

# 7. Identity Operators
a = None
if a is None:
    print("a is None")  # Output: a is None

b = 10
if b is not None:
    print("b is not None")  # Output: b is not None

# 8. One-Liner (Ternary Operator)
# Short-hand way to write an if-else condition.
x = 10
result = "Positive" if x > 0 else "Negative or Zero"
print(result)  # Output: Positive
