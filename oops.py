## Python Object-Oriented Programming (OOPs) – Complete Concepts with Inheritance Types
# OOPs allows us to structure code using classes and objects, making it modular, reusable, and scalable.

# ------------------------------------------
## 1️⃣ Class and Object
class Car:
    """This is a simple class representing a Car."""
    def __init__(self, brand, model):
        self.brand = brand  # Instance Variable
        self.model = model  # Instance Variable
    
    def show_details(self):
        """Displays car details."""
        print(f"Car: {self.brand} {self.model}")

# Creating an object
car1 = Car("Toyota", "Corolla")
car1.show_details()  # Output: Car: Toyota Corolla

# ------------------------------------------
## 2️⃣ Instance and Class Variables
class Employee:
    """This class demonstrates instance and class variables."""
    company = "TechCorp"  # Class Variable
    
    def __init__(self, name, salary):
        self.name = name  # Instance Variable
        self.salary = salary  # Instance Variable
    
    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

emp1 = Employee("Alice", 50000)
emp1.show_details()  # Output: Employee: Alice, Salary: 50000, Company: TechCorp

# ------------------------------------------
## 3️⃣ Instance, Class, and Static Methods
class MathOperations:
    """Demonstrates different types of methods."""
    
    def instance_method(self, a, b):
        return a + b  # Instance Method
    
    @classmethod
    def class_method(cls):
        return "This is a class method"
    
    @staticmethod
    def static_method():
        return "This is a static method"

math_obj = MathOperations()
print(math_obj.instance_method(5, 3))  # Output: 8
print(MathOperations.class_method())  # Output: This is a class method
print(MathOperations.static_method())  # Output: This is a static method

# ------------------------------------------
## 4️⃣ Encapsulation (Private Variables)
class BankAccount:
    """Demonstrates encapsulation by restricting direct access to sensitive data."""
    def __init__(self, balance):
        self.__balance = balance  # Private Variable
    
    def get_balance(self):
        """Provides controlled access to private variable."""
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
# print(account.__balance)  # This will raise an AttributeError

# ------------------------------------------
## 5️⃣ Inheritance (5 Types)
# 1️⃣ Single Inheritance
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    pass

obj = Child()
obj.show()  # Output: Parent class method

# 2️⃣ Multiple Inheritance
class Mother:
    def mother_feature(self):
        print("Feature from Mother")

class Father:
    def father_feature(self):
        print("Feature from Father")

class Child(Mother, Father):
    pass

obj = Child()
obj.mother_feature()  # Output: Feature from Mother
obj.father_feature()  # Output: Feature from Father

# 3️⃣ Multilevel Inheritance
class Grandparent:
    def grandparent_feature(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def parent_feature(self):
        print("Feature from Parent")

class Child(Parent):
    pass

obj = Child()
obj.grandparent_feature()  # Output: Feature from Grandparent
obj.parent_feature()  # Output: Feature from Parent

# 4️⃣ Hierarchical Inheritance
class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
obj1.show()  # Output: Parent class method
obj2.show()  # Output: Parent class method

# 5️⃣ Hybrid Inheritance (Combination of Multiple & Multilevel)
class A:
    def feature_A(self):
        print("Feature A")

class B(A):
    def feature_B(self):
        print("Feature B")

class C(A):
    def feature_C(self):
        print("Feature C")

class D(B, C):
    pass

obj = D()
obj.feature_A()  # Output: Feature A
obj.feature_B()  # Output: Feature B
obj.feature_C()  # Output: Feature C

# ------------------------------------------
## 6️⃣ Polymorphism
class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())

cat = Cat()
animal_sound(cat)  # Output: Meow
animal_sound(obj)  # Output: Feature A

# ------------------------------------------
## 7️⃣ Operator Overloading
class Vector:
    """Demonstrates operator overloading for custom objects."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# ------------------------------------------
## 8️⃣ Magic/Dunder Methods
class Person:
    """Demonstrates magic methods."""
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person({self.name})"
    
    def __call__(self):
        print(f"{self.name} has been called!")

p = Person("John")
print(p)  # Output: Person(John)
p()  # Output: John has been called!

# ------------------------------------------
