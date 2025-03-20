"""1. Arithmetic Operators (Mathematical Operations)"""

a = 15
b = 4

# Addition
add_result = a + b  
print("Addition:", add_result)  # 15 + 4 = 19

# Subtraction
sub_result = a - b  
print("Subtraction:", sub_result)  # 15 - 4 = 11

# Multiplication
mul_result = a * b  
print("Multiplication:", mul_result)  # 15 * 4 = 60

# Division (Floating-point result)
div_result = a / b  
print("Division:", div_result)  # 15 / 4 = 3.75

# Floor Division (Removes decimal part)
floor_div = a // b  
print("Floor Division:", floor_div)  # 15 // 4 = 3

# Modulus (Remainder of division)
mod_result = a % b  
print("Modulus:", mod_result)  # 15 % 4 = 3

# Exponentiation (Power)
exp_result = a ** b  
print("Exponentiation:", exp_result)  # 15 ** 4 = 50625

# Use Case: Used for mathematical calculations like finance, physics, and engineering.
#----------------------------------------------------------------------------------------------
"""2. Comparison Operators (Checking Conditions)"""

age = 20

# Checking if age is equal to 18
print(age == 18)  # False

# Checking if age is not equal to 18
print(age != 18)  # True

# Checking if age is greater than 18
print(age > 18)  # True

# Checking if age is less than 18
print(age < 18)  # False

# Checking if age is greater than or equal to 18
print(age >= 18)  # True

# Checking if age is less than or equal to 18
print(age <= 18)  # False
# Use Case: Used in authentication systems, pricing models, and decision-making.
#---------------------------------------------------------------------------------------------
"""3. Logical Operators (Combining Conditions)"""

username = "admin"
password = "1234"

# Checking if both conditions are true
if username == "admin" and password == "1234":
    print("Login Successful")  # Both conditions must be true

# Checking if at least one condition is true
if username == "admin" or password == "wrong":
    print("Login Attempt Successful")  # One condition is true

# Negating a condition
is_admin = True
print(not is_admin)  # False (negates True to False)
# Use Case: Used in user authentication, access control, and complex conditions.
#--------------------------------------------------------------------------------------
"""4. Bitwise Operators (Binary Operations)"""
x = 5  #  Binary:  0101
y = 3  #  Binary:  0011

# Bitwise AND (Both bits must be 1)
print(x & y)  # Output: 1  (Binary: 0001)

# Bitwise OR (At least one bit is 1)
print(x | y)  # Output: 7  (Binary: 0111)

# Bitwise XOR (Exclusive OR: Different bits are 1)
print(x ^ y)  # Output: 6  (Binary: 0110)

# Bitwise NOT (Inverts bits)
print(~x)  # Output: -6 (Binary: 1010 in Two's Complement)

# Left Shift (Shifts bits left, multiplying by 2)
print(x << 1)  # Output: 10  (Binary: 1010)

# Right Shift (Shifts bits right, dividing by 2)
print(x >> 1)  # Output: 2  (Binary: 0010)
# Use Case: Used in encryption, networking, and low-level programming.
#------------------------------------------------------------------------------
"""5. Assignment Operators (Shortcuts for Assigning Values)"""

points = 10

points += 5  # Same as points = points + 5
print(points)  # 15

points -= 3  # Same as points = points - 3
print(points)  # 12

points *= 2  # Same as points = points * 2
print(points)  # 24

points /= 4  # Same as points = points / 4
print(points)  # 6.0

points **= 2  # Same as points = points ** 2
print(points)  # 36.0
# Use Case: Used in counters, tracking scores, and financial calculations.
#-------------------------------------------------------------------------------------------
"""6. Identity Operators (Checking Memory Location)"""
list1 = [1, 2, 3]
list2 = list1  # Both point to the same memory
list3 = [1, 2, 3]  # Different object with the same values

print(list1 is list2)  # True (Same object)
print(list1 is list3)  # False (Different objects)
print(list1 == list3)  # True (Same values)

# Using "is not"
print(list1 is not list3)  # True (Different memory locations)
# Use Case: Used in checking object references and optimizing memory usage.
#---------------------------------------------------------------------------------------
"""7. Membership Operators (Checking Existence in a Collection)"""

names = ["Alice", "Bob", "Charlie"]

# Checking if a name is in the list
print("Alice" in names)  # True

# Checking if a name is not in the list
print("David" not in names)  # True

# Checking in a string
text = "Hello World"
print("H" in text)  # True
print("Z" in text)  # False
# Use Case: Used in searching, filtering, and recommendation systems.