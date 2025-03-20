# 1. Iterating through a list
# This loop goes through each element in the list and prints it.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 2. Iterating through a string
# This loop prints each character of the string one by one.
word = "Python"
for char in word:
    print(char)

# 3. Using range() function
# This loop iterates from 0 to 4 (5 is not included).
for i in range(5):
    print(i)

# 4. Using range() with start, stop, step
# This loop starts at 1, stops before 10, and increments by 2.
for i in range(1, 10, 2):
    print(i)

# 5. Iterating through a tuple
# This loop prints each element in the tuple.
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# 6. Iterating through a dictionary
# This loop prints key-value pairs from the dictionary.
student = {"name": "Alice", "age": 22, "course": "Python"}
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Using break in a loop
# This loop stops execution when num is 5.
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# 8. Using continue in a loop
# This loop skips printing 3 and continues with the next iteration.
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 9. Nested loops
# This generates all combinations of i and j.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 10. Using enumerate()
# This prints index and value of each item in the list.
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# 11. Using zip()
# This loops through two lists at the same time.
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# 12. List comprehension
# This creates a list of squares of numbers from 1 to 5.
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

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

# 14. Using a generator function
# This function generates numbers from 1 to n using yield.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# 15. Separating even and odd numbers
# This uses list comprehension to filter even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print("Even Numbers:", evens)
print("Odd Numbers:", odds)

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

# 17. Calculating factorial
# This calculates the factorial of 5 using a loop.
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")

# 18. Reversing a string
# This reverses the string using list comprehension.
string = "Interview"
reversed_string = "".join([string[i] for i in range(len(string)-1, -1, -1)])
print("Reversed String:", reversed_string)
