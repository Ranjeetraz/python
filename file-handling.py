# ===========================================
# 1️⃣ Opening & Closing Files
# The `open()` function is used to open a file, and `close()` is used to close it.

file = open("example.txt", "w")  # Open a file in write mode
file.write("Hello, this is a test file.")  # Write data to the file
file.close()  # Close the file

# ===========================================
# 2️⃣ Reading and Writing Files
# Different methods to read and write files.

# Writing to a file
file = open("example.txt", "w")  
file.write("Python File Handling Example.\n")
file.write("This is a second line.\n")
file.close()

# Reading from a file
file = open("example.txt", "r")  
content = file.read()  
print(content)  # Output: File content
file.close()

# ===========================================
# 3️⃣ Appending to a File (Add Method)
# Using 'a' mode to append data to an existing file.

with open("example.txt", "a") as file:
    file.write("Appending this line.\n")
    file.write("Adding another line at the end.\n")

# Reading after appending
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# ===========================================
# 4️⃣ File Handling with `with open()`
# Using `with open()` ensures files are closed automatically.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: File content

# Writing with `with open()`
with open("example.txt", "w") as file:
    file.write("New content using 'with open()'.\n")

# ===========================================
# 5️⃣ Working with CSV Files
# Using the `csv` module to read and write CSV files.

import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Los Angeles"])

# Appending data to CSV file
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 35, "Chicago"])

# Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ===========================================
# 6️⃣ Working with JSON Files
# Using the `json` module to read and write JSON files.

import json

# Writing to a JSON file
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Appending to a JSON file (Read-Modify-Write)
with open("data.json", "r") as file:
    data = json.load(file)

data["country"] = "USA"  # Adding a new key-value pair

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading from a JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Output: Updated JSON content

# ===========================================
# 7️⃣ Working with Config Files (`configparser`)
# Using `configparser` to manage configuration files.

import configparser

# Creating a config file
config = configparser.ConfigParser()
config["Settings"] = {
    "theme": "dark",
    "language": "English"
}

with open("config.ini", "w") as file:
    config.write(file)

# Appending to config file (Adding a new section)
config["User"] = {
    "username": "admin",
    "role": "editor"
}

with open("config.ini", "w") as file:
    config.write(file)

# Reading from a config file
config.read("config.ini")
print(config["Settings"]["theme"])  # Output: dark
print(config["User"]["username"])  # Output: admin
