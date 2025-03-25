"""
Python Pattern Program: Right-Angled, Inverted Right-Angled & Pyramid Triangle
Author: Your Name
Date: 2025

This script demonstrates the creation of right-angled, inverted right-angled, and pyramid triangle patterns using nested loops.
"""

# Right-Angled Triangle Pattern
print("Right-Angled Triangle Pattern")

# Outer loop controls the number of rows
for i in range(6):  # Runs from 0 to 5 (total 6 rows)
    
    # Inner loop controls the number of stars printed per row
    for j in range(i + 1):  # Prints (i+1) stars in each row
        print("*", end=" ")  # Print star with space, staying on the same line
    
    print()  # Move to the next line after printing stars for a row

"""
Explanation:
1. The outer loop runs from `i = 0` to `i = 5`, creating 6 rows.
2. The inner loop runs from `j = 0` to `j = i`, printing `i+1` stars per row.
3. `print("*", end=" ")` ensures stars are printed on the same line.
4. The `print()` statement moves to the next line after printing stars for each row.

Expected Output:
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""

# Inverted Right-Angled Triangle Pattern
print("\nInverted Right-Angled Triangle")

# Outer loop controls the number of rows in decreasing order
for i in range(6):  # Runs from 0 to 5
    
    # Inner loop prints decreasing number of stars
    for j in range(6 - i):  # Prints (6-i) stars in each row
        print("*", end=" ")  # Print star with space, staying on the same line
    
    print()  # Move to the next line after printing stars for a row

"""
Explanation:
1. The outer loop runs from `i = 0` to `i = 5`, creating 6 rows.
2. The inner loop runs from `j = 0` to `j < 6 - i`, printing decreasing stars in each row.
3. `print("*", end=" ")` ensures stars are printed on the same line.
4. The `print()` statement moves to the next line after printing stars for each row.

Expected Output:
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""

# Pyramid Pattern
print("\nPyramid Pattern")

# Outer loop controls the number of rows
for i in range(1, 6):  # Runs from 1 to 5
    
    # Printing spaces to align the pyramid
    for j in range(5 - i):  # Controls spaces before stars
        print(" ", end=" ")
    
    # Printing left-side stars
    for m in range(i):  
        print("*", end=" ")
    
    # Printing right-side stars
    for m in range(i - 1):  
        print("*", end=" ")
    
    print()  # Move to next line

"""
Explanation:
1. The outer loop runs from `i = 1` to `i = 5`, controlling the number of rows.
2. The first inner loop adds spaces for pyramid alignment.
3. The second inner loop prints the left-side stars.
4. The third inner loop prints the right-side stars.
5. The `print()` statement moves to the next line.

Expected Output:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

# Opposite Pyramid Pattern
print("\nOpposite Pyramid Pattern")

# Outer loop controls the number of rows
for i in range(5, 0, -1):  # Runs from 5 to 1
    
    # Printing spaces to align the inverted pyramid
    for j in range(5 - i):  # Controls spaces before stars
        print(" ", end=" ")
    
    # Printing left-side stars
    for m in range(i):  
        print("*", end=" ")
    
    # Printing right-side stars
    for m in range(i - 1):  
        print("*", end=" ")
    
    print()  # Move to next line

"""
Explanation:
1. The outer loop runs from `i = 5` to `i = 1`, controlling the number of rows.
2. The first inner loop adds spaces for inverted pyramid alignment.
3. The second inner loop prints the left-side stars.
4. The third inner loop prints the right-side stars.
5. The `print()` statement moves to the next line.

Expected Output:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

# Diamond Pattern
print("\nDiamond Pattern")

# Upper part of diamond
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for m in range(i):
        print("*", end=" ")
    for m in range(i - 1):
        print("*", end=" ")
    print()

# Lower part of diamond
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end=" ")
    for m in range(i):
        print("*", end=" ")
    for m in range(i - 1):
        print("*", end=" ")
    print()

"""
Explanation:
1. The first loop generates the upper pyramid.
2. The second loop generates the lower inverted pyramid.
3. Spaces are added for alignment.
4. The output forms a symmetric diamond shape.

Expected Output:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

"""
How to Run this Script:
1. Save this file as 'triangle_patterns.py'.
2. Open a terminal or command prompt.
3. Run the script using the command: `python triangle_patterns.py`.
4. All six triangle patterns will be displayed on the console.
"""
