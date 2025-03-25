# Factorial Calculation
print("\nFactorial Calculation")

num = 5  # Change this number to calculate factorial of any other number
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} using iterative method is: {factorial}")
"""
Output:
Factorial Calculation
Factorial of 5 using iterative method is: 120
"""