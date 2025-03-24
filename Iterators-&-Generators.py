## Python Iterators & Generators – Complete Guide with Examples
# Iterators and Generators allow us to process sequences efficiently.

# ------------------------------------------
## 1️⃣ Creating an Iterator
# Definition: An iterator must implement the __iter__() and __next__() methods.

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self  # Returns the iterator object itself
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Stops iteration when limit is reached
        value = self.current
        self.current += 1
        return value

# Using the iterator
iter_obj = MyIterator(1, 5)
for num in iter_obj:
    print(num)  # Output: 1, 2, 3, 4

# ------------------------------------------
## 2️⃣ Creating a Generator
# Definition: A generator function uses 'yield' instead of 'return'.

def my_generator(start, end):
    while start < end:
        yield start  # Yields the current value and pauses execution
        start += 1

# Using the generator
gen_obj = my_generator(1, 5)
for num in gen_obj:
    print(num)  # Output: 1, 2, 3, 4

# ------------------------------------------
## 3️⃣ Generator with Multiple Yields
# Definition: A generator can yield multiple values at different stages.

def multiple_yield_generator():
    yield "First value"
    yield "Second value"
    yield "Third value"

# Using the generator
gen = multiple_yield_generator()
print(next(gen))  # Output: First value
print(next(gen))  # Output: Second value
print(next(gen))  # Output: Third value

# ------------------------------------------
## 4️⃣ Infinite Generator
# Definition: Generators can create infinite sequences if needed.

def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1

# Using the generator (be careful with infinite loops)
inf_gen = infinite_counter()
print(next(inf_gen))  # Output: 1
print(next(inf_gen))  # Output: 2
print(next(inf_gen))  # Output: 3

# ------------------------------------------
## 5️⃣ Generator Expressions
# Definition: A compact way to create generators.

# Generator Expression Example
squares = (x * x for x in range(1, 6))
print(next(squares))  # Output: 1
print(next(squares))  # Output: 4
print(next(squares))  # Output: 9

# ------------------------------------------
## 6️⃣ Using Generators for Large Data Processing
# Definition: Generators are useful for handling large datasets efficiently.

def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Reads and yields one line at a time

# Example usage (Assuming large_file.txt exists)
# for line in read_large_file("large_file.txt"):
#     print(line)  # Prints each line without loading the whole file in memory

# ------------------------------------------
## 7️⃣ Chaining Generators
# Definition: Generators can be combined for more complex pipelines.

def generator1():
    yield from range(1, 4)

def generator2():
    yield from range(4, 7)

def combined_generators():
    yield from generator1()
    yield from generator2()

for num in combined_generators():
    print(num)  # Output: 1, 2, 3, 4, 5, 6

# ------------------------------------------
## 8️⃣ Fibonacci Sequence using Generator
# Definition: A generator can be used to generate Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the Fibonacci generator
for num in fibonacci(10):
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
