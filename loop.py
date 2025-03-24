# 1. Iterating through a list
# This loop goes through each element in the list and prints it.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Output: 1, 2, 3, 4, 5

# 2. Iterating through a string
# This loop prints each character of the string one by one.
word = "Python"
for char in word:
    print(char)
# Output: P, y, t, h, o, n

# 3. Using range() function
# This loop iterates from 0 to 4 (5 is not included).
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# 4. Using range() with start, stop, step
# This loop starts at 1, stops before 10, and increments by 2.
for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9

# 5. Iterating through a tuple
# This loop prints each element in the tuple.
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# 6. Iterating through a dictionary
# This loop prints key-value pairs from the dictionary.
student = {"name": "Alice", "age": 22, "course": "Python"}
for key, value in student.items():
    print(f"{key}: {value}")
# Output: name: Alice, age: 22, course: Python

# 7. Using break in a loop
# This loop stops execution when num is 5.
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# Output: 1, 2, 3, 4

# 8. Using continue in a loop
# This loop skips printing 3 and continues with the next iteration.
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# Output: 1, 2, 4, 5

# 9. Nested loops
# This generates all combinations of i and j.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
# Output: i=1, j=1, i=1, j=2, i=1, j=3, i=2, j=1, i=2, j=2, i=2, j=3, i=3, j=1, i=3, j=2, i=3, j=3

# 10. Using enumerate()
# This prints index and value of each item in the list.
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
# Output: 0: Alice, 1: Bob, 2: Charlie

# 11. Using zip()
# This loops through two lists at the same time.
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# Output: Alice is 25 years old., Bob is 30 years old., Charlie is 22 years old.

# 12. List comprehension
# This creates a list of squares of numbers from 1 to 5.
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
# Output: Squares: [1, 4, 9, 16, 25]

# Using if Condition in List Comprehension
# Example: Filtering even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8]

# 3. Using if-else in List Comprehension
# Example: Categorizing numbers as even or odd
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']


# 13. Creating a custom iterable class
# This class defines an iterable that counts from 1 to 5.
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

numbers = MyNumbers()
for num in numbers:
    print(num)
# Output: 1, 2, 3, 4, 5

# 14. Using a generator function
# This function generates numbers from 1 to n using yield.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
# Output: 1, 2, 3, 4, 5

# 15. Separating even and odd numbers
# This uses list comprehension to filter even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print("Even Numbers:", evens)
print("Odd Numbers:", odds)
# Output: Even Numbers: [2, 4, 6, 8, 10]
# Output: Odd Numbers: [1, 3, 5, 7, 9]

# 16. Finding prime numbers
# This function checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 20) if is_prime(num)]
print("Prime Numbers:", primes)
# Output: Prime Numbers: [2, 3, 5, 7, 11, 13, 17, 19]

# 17. Calculating factorial
# This calculates the factorial of 5 using a loop.
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
# Output: Factorial of 5 is 120

# 18. Reversing a string
# This reverses the string using list comprehension.
string = "Interview"
reversed_string = "".join([string[i] for i in range(len(string)-1, -1, -1)])
print("Reversed String:", reversed_string)
# Output: Reversed String: weivretnI
