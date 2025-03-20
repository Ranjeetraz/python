"""int data type"""
# a = 10        # positive integer
# b = -5        # negative integer
# c = 0         # zero
# d = "22"      # String
# print(type(a))


# print(int(True))   # Output: 1
# print(int(False))  # Output: 0


"""Arithmetic Operators"""
# x = 10
# y = 3
# sum_result = x + y          # Addition
# difference = x - y         # Subtraction
# product = x * y            # Multiplication
# quotient = x / y           # Division (returns float)
# remainder = x % y          # Modulus (remainder)
# floor_div = x // y         # Floor Division (returns integer)
# power = x ** y             # Exponentiation (x raised to the power y)
# print("x = ",10,",y = ",3)
# print("Addition:", sum_result)
# print("Subtraction:", difference)
# print("Multiplication:", product)
# print("Division (returns float):", quotient)
# print("Remainder (Modulus):", remainder)
# print("Floor Division:", floor_div)
# print("Exponentiation:", power)

"""Bitwise Operations"""
# a = 5  # Binary: 101
# b = 3  # Binary: 011

# print("Bitwise AND:", a & b)  # Output: 1 (001)
# print("Bitwise OR:", a | b)   # Output: 7 (111)
# print("Bitwise XOR:", a ^ b)  # Output: 6 (110)
# print("Left Shift (5 << 1):", a << 1)  # 10 (1010)
# print("Right Shift (5 >> 1):", a >> 1) # 2 (10)


# -----------------------------------------------------------------------------------
"""float data type"""
# x = 10.5   # Positive float
# y = -3.14  # Negative float
# z = 0.0    # Zero as a float

# print(x, y, z)
# print(type(x))  # Output: <class 'float'>

"""Type casting, also known as type conversion, is the process of changing a variable's data type to another data type in Python. """
# num = 10
# float_num = float(num)  # Converts int to float

# print(float_num)   # Output: 10.0
# print(type(float_num))  # Output: <class 'float'>

# ----------------------------------------------------------------------
"""complex data type"""
"""Direct Assignment"""
# z = 3 + 4j
# print(z)  # Output: (3+4j)
# print(type(z))  # Output: <class 'complex'>

"""Using complex() Function"""
# z1 = complex(3, 4)  # 3 is real part, 4 is imaginary part
# print(z1)  # Output: (3+4j)

"""Accessing Real and Imaginary Parts"""
# z = 5 + 7j
# print("Real Part:", z.real)  # Output: 5.0
# print("Imaginary Part:", z.imag)  # Output: 7.0

"""Basic Operations on Complex Numbers"""
# a = 2 + 3j
# b = 1 + 4j

# print("Addition:", a + b)         # (3+7j)
# print("Subtraction:", a - b)      # (1-1j)
# print("Multiplication:", a * b)   # (-10+11j)
# print("Division:", a / b)         # (0.8235-0.2941j)

"""Complex Conjugate
Complex संख्या का conjugate वह संख्या होती है, जिसमें काल्पनिक भाग का चिन्ह बदल दिया जाता है।
🔹 conjugate() मेथड का उपयोग करें"""
# z = 3 + 4j
# print("Conjugate:", z.conjugate())  # Output: (3-4j)

# ---------------------------------------------------------
"""Python bool/Boolean Data Type"""
# x = True
# y = False
# print(x, y)  # Output: True False
# print(type(x))  # Output: <class 'bool'>

"""omparison operators return Boolean (True or False)."""
# print(5 > 3)   # True
# print(10 == 5)  # False
# print(4 != 2)  # True
# print(7 <= 7)  # True

# --------------String Data type--------------------------------------------
"""str (String - Text Data)
Stores text data, which is a sequence of characters.
Written inside single, double, or triple quotes.
Strings are immutable, meaning once created, they cannot be modified.
Supports indexing (accessing individual characters) and slicing (extracting parts of a string).
Used in handling text, storing names, messages, and any character-based data.
"""
"""Indexing allows access to individual characters in a string.
Starts from 0 (positive indexing) and -1 (negative indexing for reverse)."""

"""सभी Python String Methods की लिस्ट और उनका उपयोग
(A) Case Conversion Methods (कैपिटल और स्मॉल लेटर बदलने के लिए)
✅ upper() → पूरे string को uppercase (बड़े अक्षरों) में बदलता है।
✅ lower() → पूरे string को lowercase (छोटे अक्षरों) में बदलता है।
✅ casefold() → lowercase में बदलता है, लेकिन special characters के लिए बेहतर होता है।
✅ capitalize() → सिर्फ पहले अक्षर को uppercase करता है, बाकी lowercase होते हैं।
✅ title() → हर शब्द के पहले अक्षर को uppercase करता है।
✅ swapcase() → uppercase को lowercase और lowercase को uppercase में बदलता है।
(B) Checking Properties (स्ट्रिंग की विशेषताएँ जांचने के लिए)
✅ isupper() → चेक करता है कि क्या सभी अक्षर uppercase हैं।
✅ islower() → चेक करता है कि क्या सभी अक्षर lowercase हैं।
✅ istitle() → चेक करता है कि क्या हर शब्द के पहले अक्षर uppercase हैं।
✅ isalpha() → चेक करता है कि क्या सभी characters alphabetic हैं (a-z, A-Z)।
✅ isdigit() → चेक करता है कि क्या सभी characters digits हैं (0-9)।
✅ isalnum() → चेक करता है कि क्या सभी characters alphabetic या numeric हैं।
✅ isspace() → चेक करता है कि क्या string में सिर्फ spaces हैं।
✅ isascii() → चेक करता है कि string में सिर्फ ASCII characters हैं।
✅ isprintable() → चेक करता है कि string में केवल प्रिंटेबल characters हैं।
✅ isidentifier() → चेक करता है कि string एक valid Python variable नाम हो सकता है या नहीं।
(C) Searching & Finding Methods (स्ट्रिंग में खोजने के लिए)
✅ startswith(substring) → चेक करता है कि string एक दिए गए substring से शुरू होती है या नहीं।
✅ endswith(substring) → चेक करता है कि string एक दिए गए substring से खत्म होती है या नहीं।
✅ find(substring) → substring का पहला स्थान (index) लौटाता है, अगर नहीं मिला तो -1।
✅ index(substring) → substring का पहला स्थान (index) देता है, लेकिन नहीं मिलने पर error देता है।
✅ count(substring) → substring कितनी बार आता है, यह बताता है।
(D) Modify & Replace Methods (स्ट्रिंग को बदलने के लिए)
✅ replace(old, new) → string में एक word को दूसरे से बदलता है।
✅ removeprefix(prefix) → string के शुरू में से दिए गए prefix को हटाता है।
✅ removesuffix(suffix) → string के अंत में से दिए गए suffix को हटाता है।
(E) String Formatting (स्ट्रिंग को बेहतर फॉर्मेट करने के लिए)
✅ format() → placeholders {} के जरिए string को फॉर्मेट करता है।
✅ f-strings → f"{variable}" के जरिए string को फॉर्मेट करता है।
✅ zfill(width) → string की लंबाई को बढ़ाकर leading zeros (0) जोड़ता है।
(F) String Splitting & Joining (स्ट्रिंग को तोड़ना और जोड़ना)
✅ split(separator) → string को एक list में बदलता है।
✅ rsplit(separator, maxsplit) → दाएं से split करता है।
✅ splitlines() → multi-line string को lines की list में बदलता है।
✅ join(iterable) → list को एक string में जोड़ता है।
(G) Whitespace & Trimming Methods (स्पेस हटाने के लिए)
✅ strip() → string के start और end के spaces को हटाता है।
✅ lstrip() → string के start के spaces को हटाता है।
✅ rstrip() → string के end के spaces को हटाता है।
(H) Escape Characters (स्पेशल कैरेक्टर्स दिखाने के लिए)
✅ \' → Single quote को दिखाने के लिए।
✅ \" → Double quote को दिखाने के लिए।
✅ \\ → Backslash दिखाने के लिए।
✅ \n → New line (अगली लाइन में जाने के लिए)।
✅ \t → Tab space देने के लिए।
(I) String Slicing & Indexing (स्ट्रिंग के कुछ हिस्से एक्सट्रैक्ट करने के लिए)

Parameter
विवरण
start
वह index जहाँ से slicing शुरू होगी (default: 0)
end
वह index जहाँ तक slicing होगी (exclusive, यानी end शामिल नहीं होता)
step
कितने characters को skip करना है (default: 1)


✅ s[start:end:step] → string के किसी हिस्से को निकालने के लिए।
✅ s[::-1] → string को reverse करने के लिए।
(J) Other Useful Methods (अन्य उपयोगी मेथड्स)
✅ len(string) → string की लंबाई (characters की संख्या) निकालने के लिए।
✅ min(string) → string में सबसे छोटा character (ASCII value के अनुसार)।
✅ max(string) → string में सबसे बड़ा character (ASCII value के अनुसार)।
✅ ord(character) → किसी character की ASCII value देने के लिए।
✅ chr(number) → ASCII number से character बनाने के लिए।"""

a = "RANJEET, kumar, Raj, kumar"
b = "22"
w = "year old"

"""Uppercase conversion (सभी अक्षर uppercase में)"""
print(a.upper())  # RANJEET, KUMAR, RAJ, KUMAR

"""Lowercase conversion (सभी अक्षर lowercase में)"""
print(a.lower())  # ranjeet, kumar, raj, kumar

"""Casefold (lowercase conversion, खासकर special characters के लिए बेहतर)"""
print(a.casefold())  # ranjeet, kumar, raj, kumar

"""Capitalize (सिर्फ पहले अक्षर को capitalize करेगा, बाकी lowercase रहेंगे)"""
print(a.capitalize())  # Ranjeet, kumar, raj, kumar

"""Title case (हर शब्द के पहले अक्षर को capitalize करेगा)"""
print(a.title())  # Ranjeet, Kumar, Raj, Kumar

"""Swapcase (uppercase को lowercase और lowercase को uppercase करेगा)"""
print(a.swapcase())  # ranjeet, KUMAR, rAJ, KUMAR

"""Check if string starts with "RANJEET" """
print(a.startswith("RANJEET"))  # True

"""Check if string ends with "kumar" """
print(a.endswith("kumar"))  # True

"""Find the index of first occurrence of "kumar" """
print(a.find("kumar"))  # 9

"""Find index of first occurrence of "k" """
print(a.index("k"))  # 9

"""Count occurrences of "kumar" """
print(a.count("kumar"))  # 2

"""Replace "RANJEET" with "Manish" """
print(a.replace("RANJEET", "Manish"))  # Manish, kumar, Raj, kumar

"""Center align string in 60 characters"""
print(a.center(60))  # '      RANJEET, kumar, Raj, kumar                   '

"""Concatenation of strings (सभी स्ट्रिंग्स को जोड़ना)"""
print(a + " " + b + " " + w)  # RANJEET, kumar, Raj, kumar 22 year old

"""String repetition (स्ट्रिंग को कई बार दोहराना)"""
print(a * 2)  # RANJEET, kumar, Raj, kumarRANJEET, kumar, Raj, kumar

"""Slicing: Extract first 7 characters"""
print(a[0:7])  # RANJEET

"""Reverse slicing: Extract last 10 characters in reverse order"""
print(a[-1:-11:-1])  # ramuk ,jar

"""Selective slicing"""
print(a[0:7], a[16:19], a[21:26])  # RANJEET Raj kumar

# Check if all characters are uppercase
print(a.isupper())  # False

"""Check if all characters in `w` are lowercase"""
print(w.islower())  # True

"""Check if `a` follows title case format"""
print(a.istitle())  # False

"""Check if `b` is numeric"""
print(b.isnumeric())  # True

"""Check if `b` contains only digits"""
print(b.isdigit())  # True

"""Check if `a` is alphabetic"""
print(a.isalpha())  # False (क्योंकि इसमें स्पेस और कॉमा हैं)

"""Check if `b` is alphanumeric"""
print(b.isalnum())  # True (सिर्फ संख्या और अक्षर होने चाहिए)

"""Check if `a` contains only spaces"""
empty_string = "   "
print(empty_string.isspace())  # True

"""String length using len()"""
print(len(a))  # 26

"""Removing extra spaces"""
s = "   Hello World   "
print(s.strip())   # 'Hello World'
print(s.lstrip())  # 'Hello World   '
print(s.rstrip())  # '   Hello World'

"""Splitting a string into a list"""
s = "apple,banana,grape"
words = s.split(",")  # ['apple', 'banana', 'grape']
print(words)

"""Joining list elements into a string"""
new_s = "-".join(words)  # 'apple-banana-grape'
print(new_s)

"""Checking if a substring exists in a string"""
print("kumar" in a)  # True
print("Python" not in a)  # True

"""Count occurrences of a character"""
print(a.count("a"))  # 3

"""Convert list to string"""
words_list = ["Python", "is", "fun"]
sentence = " ".join(words_list)
print(sentence)  # 'Python is fun'

"""Convert string to list"""
sentence = "Python is fun"
words = sentence.split()
print(words)  # ['Python', 'is', 'fun']

"""String Iteration"""
for char in a:
    print(char, end=" ")  # R A N J E E T , k u m a r , R a j , k u m a r

"""String Formatting (f-strings)"""
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")  # My name is John and I am 25 years old.

"""Reverse a string"""
print(a[::-1])  # rumak ,jaR ,ramuk ,TEEJNAR

"""Padding zeros (leading zeros)"""
num = "5"
print(num.zfill(3))  # 005

"""Capitalize first letter of each word"""
sentence = "hello world! python is great."
print(sentence.title())  # 'Hello World! Python Is Great.'


# -----------------list-------------------------------------------------
"""
list (List - Changeable Collection)
Stores multiple items in a specific order.
Can hold different data types, including numbers, strings, and even other lists.
Lists are mutable, meaning elements can be changed, added, or removed after creation.
Supports indexing and slicing like strings.
Used in scenarios where data needs to be stored dynamically and modified frequently.

"""
# ============================================
# (A) Adding Elements (append, extend, insert, + operater)
# ============================================

"""append यह एक argument लेता है और लिस्ट के अंत में जोड़ता है"""
fruits = ["apple", "banana"]
a = [45,67,89]
fruits.append(a) # Output: ['apple', 'banana', [45, 67, 89]]
fruits.append([34,56,78,90]) # Output: ['apple', 'banana', [34, 56, 78, 90]]
fruits.append("mango")  # Output: ['apple', 'banana', 'mango']  
print(fruits) 

"""extend एक iterable के सभी एलिमेंट्स को लिस्ट में जोड़ता है"""
list1 = [1, 2, 3]
list1.extend([4, 5, 6]) #Output: [1, 2, 3, 4, 5, 6]
list1.extend("iterable") #Output: [1, 2, 3, 'i', 't', 'e', 'r', 'a', 'b', 'l', 'e'
list2 = [2,3,5,]
list1.extend(list2) #Output: [1, 2, 3, 2, 3, 5]
print(list1) 

"""insert दिए गए index पर एक एलिमेंट जोड़ता है"""
list1 = [1, 2, 3]
list1.insert(2, 10)  #Output: [1, 2, 10, 3]
list2 = [6,7,8]
list1.insert(2, list2)  #Output: [1, 2, [6, 7, 8], 3]
print(list1)

"""+= ऑपरेटर का उपयोग करके लिस्ट में एलिमेंट्स जोड़ना"""
list1 += [7, 8, 9]  
print(f"+= operator: {list1}")  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# ============================================
# (B) Removing Elements (एलिमेंट्स हटाना)
# ============================================

"""remove एक argument लेता है, केवल पहला मैचिंग एलिमेंट हटाता है"""
colors = ["red", "blue", "green", "blue"]
colors.remove("blue")  
print(f"remove: {colors}")  # Output: ['red', 'green', 'blue']

"""pop दिए गए index का एलिमेंट हटाकर return करता है"""
nums = [10, 20, 30, 40]
popped = nums.pop(2) 
nums.pop() #output: 40
print(f"pop: {nums}, popped: {popped}")  # Output: [10, 20, 40], 30

"""clear पूरी लिस्ट को खाली कर देता है"""
data = [1, 2, 3]
data.clear()  
print(f"clear: {data}")  # Output: []

"""del ऑपरेटर से index का एलिमेंट स्थायी रूप से delete कर सकते हैं"""
nums = [10, 20, 30, 40]
del nums[0]  
print(nums)  # Output: [20, 30, 40]

# ============================================
# (C) Searching & Counting (खोज और गिनती)
# ============================================

"""index पहला मैचिंग एलिमेंट का index देता है"""
animals = ["cat", "dog", "rabbit", "dog"]
pos = animals.index("dog")  
print(pos)  # Output: 1

"""count किसी वैल्यू की कुल occurrences बताता है"""
numbers = [1, 2, 3, 1, 1, 4]
count_1 = numbers.count(1)  
print(count_1)  # Output: 3

# ============================================
# (D) Sorting & Reversing (क्रमबद्ध करना और उलटना)
# ============================================

"""sort() लिस्ट को ascending क्रम में sort करता है"""
values = [5, 2, 9, 1]
values.sort()  
print(values)  # Output: [1, 2, 5, 9]

"""sort(reverse=True) लिस्ट को descending क्रम में sort करता है"""
values.sort(reverse=True)  
print(values)  # Output: [9, 5, 2, 1]

"""reverse() लिस्ट के सभी एलिमेंट्स को उलट देता है"""
items = ["a", "b", "c"]
items.reverse()  
print(f"reverse: {items}")  # Output: ['c', 'b', 'a']

# ============================================
# (E) Copying Lists (लिस्ट कॉपी करना)
# ============================================

"""copy() लिस्ट की shallow copy बनाता है"""
original = [1, 2, 3]
duplicate = original.copy()  
print(f"copy: {duplicate}")  # Output: [1, 2, 3]

"""deepcopy() एक deep copy बनाता है"""
import copy
deep_copy_list = copy.deepcopy(original)  
print(f"deepcopy: {deep_copy_list}")  # Output: [1, 2, 3]

# ============================================
# (F) List Operations (लिस्ट ऑपरेशन)
# ============================================

"""len() लिस्ट की लंबाई देता है"""
length = len(numbers)  
print(f"len: {length}")  # Output: 6

"""min() और max() लिस्ट के सबसे छोटे और बड़े एलिमेंट्स देते हैं"""
minimum = min(values)  
print(f"min: {minimum}")  # Output: 1

maximum = max(values)  
print(f"max: {maximum}")  # Output: 9

"""sum() सभी संख्यात्मक एलिमेंट्स का योग देता है"""
total = sum(numbers)  
print(f"sum: {total}")  # Output: 12

# ============================================
# (G) List Comprehension (लिस्ट संक्षिप्त रूप में बनाना)
# ============================================
"""if condition comes after the for loop/if-else condition must be placed before the for loop"""
n1 = [x if x%2==0 else "even" for x in range(12)]  # Output: [0, 'even', 2, 'even', 4, 'even', 6, 'even', 8, 'even', 10, 'even']
n1 = [x for x in range(12) if x%2==0] # Output: [0, 2, 4, 6, 8, 10]
print(n1) 

# ============================================
# (H) Joining & Splitting (जोड़ना और विभाजित करना)
# ============================================

"""join() लिस्ट को स्ट्रिंग में बदलता है"""
words = ["hello", "world"]
sentence = " ".join(words)  
print(f"join: {sentence}")  # Output: 'hello world'

"""split() स्ट्रिंग को लिस्ट में बदलता है"""
text = "apple,banana,grape"
fruits_list = text.split(",")  
print(f"split: {fruits_list}")  # Output: ['apple', 'banana', 'grape']

# ============================================
# (I) Other Useful Methods (अन्य उपयोगी मेथड्स)
# ============================================

"""list() किसी भी iterable को लिस्ट में बदलता है"""
tuple_data = (1, 2, 3)
list_data = list(tuple_data)  
print(f"list(): {list_data}")  # Output: [1, 2, 3]

# ============================================
# (K) Functional Programming (फंक्शनल प्रोग्रामिंग)
# ============================================

"""filter() और map() का उपयोग"""
filtered_list = list(filter(lambda x: x % 2 == 0, numbers))  
print(f"filter: {filtered_list}")  # Output: [2, 4]

mapped_list = list(map(lambda x: x * 2, numbers))  
print(f"map: {mapped_list}")  # Output: [2, 4, 6, 2, 2, 8]


"""
(A) Adding Elements
✅append(value) → लिस्ट के अंत में एक नया एलिमेंट जोड़ता है।
✅extend(iterable) → किसी दूसरी लिस्ट या iterable के सभी एलिमेंट्स को मौजूदा लिस्ट में जोड़ता है।
✅insert(index, value) → दिए गए इंडेक्स पर एक नया एलिमेंट जोड़ता है।
✅+= (concatenation) → दो लिस्ट को जोड़ने के लिए उपयोग किया जाता है।
(B) Removing Elements
✅remove(value) → लिस्ट में दी गई वैल्यू का पहला मैचिंग एलिमेंट हटाता है।
✅pop(index) → दिए गए इंडेक्स से एलिमेंट को हटाकर उसे रिटर्न करता है।
✅clear() → पूरी लिस्ट को खाली कर देता है, यानी सभी एलिमेंट्स को हटा देता है।
✅del list[index] → दिए गए इंडेक्स का एलिमेंट स्थायी रूप से हटा देता है।
(C) Searching & Counting
✅index(value) → दिए गए एलिमेंट का पहला इंडेक्स लौटाता है, नहीं मिलने पर Error देता है।
✅count(value) → लिस्ट में किसी वैल्यू की कुल संख्या बताता है।
✅in (membership test) → चेक करता है कि कोई वैल्यू लिस्ट में मौजूद है या नहीं।
(D) Sorting & Reversing
✅sort() → लिस्ट को ascending (बढ़ते) क्रम में व्यवस्थित करता है।
✅sort(reverse=True) → लिस्ट को descending (घटते) क्रम में व्यवस्थित करता है।
✅sorted(list) → एक नई sorted लिस्ट लौटाता है, मूल लिस्ट अपरिवर्तित रहती है।
✅reverse() → लिस्ट के सभी एलिमेंट्स को उलट देता है।
(E) Copying Lists
✅copy() → लिस्ट की एक शैलो (浅) कॉपी बनाता है।
✅list(original) → लिस्ट की कॉपी बनाने का एक अन्य तरीका।
✅copy.deepcopy(list) → एक deep copy बनाता है, जिससे सबलिस्ट भी कॉपी हो जाती हैं।
(F) List Operations
✅len(list) → लिस्ट की लंबाई (एलिमेंट्स की संख्या) बताता है।
✅min(list) → लिस्ट में सबसे छोटा एलिमेंट बताता है।
✅max(list) → लिस्ट में सबसे बड़ा एलिमेंट बताता है।
✅sum(list) → लिस्ट के सभी संख्यात्मक एलिमेंट्स का योग देता है।
(G) List Comprehension
✅[expression for item in iterable] → संक्षिप्त रूप में लिस्ट बनाने का तरीका।
✅[x**2 for x in range(5)] → [0, 1, 4, 9, 16] जैसी नई लिस्ट बनाता है।
(H) Joining & Splitting
✅"separator".join(list) → लिस्ट के सभी एलिमेंट्स को एक स्ट्रिंग में जोड़ता है।
✅string.split(separator) → स्ट्रिंग को दिए गए सेपरेटर के आधार पर एक लिस्ट में बदलता है।
(I) Other Useful Methods
✅list(tuple_data) → टपल को लिस्ट में बदलता है।
✅any(list) → अगर लिस्ट में कोई भी True वैल्यू हो तो True लौटाता है।
✅all(list) → अगर लिस्ट के सभी वैल्यू True हों तो True लौटाता है।
(J) Enumerate & Zip
✅enumerate(list) → लिस्ट को index-value pairs में बदलता है।
✅zip(list1, list2) → दो लिस्ट को tuple pairs में जोड़ता है।
(K) Functional Programming
✅filter(function, list) → एक नई लिस्ट बनाता है जिसमें सिर्फ True वैल्यू वाले एलिमेंट होते हैं।
✅map(function, list) → सभी एलिमेंट्स पर function लगाकर नई लिस्ट बनाता है।
"""
# -----------------Tuple----------------------------------------------------------
"""
tuple (Tuple - Fixed Collection)
Similar to a list but immutable, meaning its values cannot be changed after creation.
More memory-efficient and faster than lists.
Used when you want to store a fixed collection of values that should not be altered.
Supports indexing and slicing, just like lists.

"""

# Tuple Methods in Python

# 1. count() - यह मेथड किसी विशेष तत्व (element) की टपल में कितनी बार उपस्थिति है, उसे गिनता है।
tuple1 = (10, 20, 30, 10, 10, 40, 50)
count_10 = tuple1.count(10)  # 10 तीन बार आता है
print("Count of 10:", count_10)

# 2. index() - यह मेथड किसी विशेष तत्व का पहला इंडेक्स लौटाता है।
tuple2 = (5, 10, 15, 20, 25, 10, 30)
index_10 = tuple2.index(10)  # पहला 10 इंडेक्स 1 पर स्थित है
print("Index of first occurrence of 10:", index_10)

# Tuple के अन्य महत्वपूर्ण ऑपरेशन (हालाँकि टपल immutable होते हैं, फिर भी कुछ ऑपरेशन संभव हैं)

# 3. Tuple Concatenation (टपल को जोड़ना)
tuple3 = (1, 2, 3)
tuple4 = (4, 5, 6)
concatenated_tuple = tuple3 + tuple4  # नया टपल बनेगा
print("Concatenated Tuple:", concatenated_tuple)

# 4. Tuple Repetition (टपल को गुणा करना)
tuple5 = ("Hello",) * 3  # टपल को तीन बार रिपीट करेंगे
print("Repeated Tuple:", tuple5)

# 5. Membership Check (टपल में तत्व मौजूद है या नहीं)
tuple6 = (100, 200, 300, 400)
print("Is 200 in tuple?", 200 in tuple6)  # True लौटाएगा
print("Is 500 in tuple?", 500 in tuple6)  # False लौटाएगा

# 6. Tuple Slicing (टपल के कुछ हिस्सों को निकालना)
tuple7 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Sliced Tuple (2:6):", tuple7[2:6])  # इंडेक्स 2 से 5 तक के तत्व
print("Sliced Tuple (:4):", tuple7[:4])  # शुरुआत से इंडेक्स 3 तक के तत्व
print("Sliced Tuple (5:):", tuple7[5:])  # इंडेक्स 5 से अंत तक के तत्व
print("Sliced Tuple with Step (1:8:2):", tuple7[1:8:2])  # स्टेप 2 के साथ स्लाइसिंग

# 7. Tuple Unpacking (टपल को अलग-अलग वेरिएबल्स में बांटना)
tuple8 = ("Apple", "Banana", "Cherry")
fruit1, fruit2, fruit3 = tuple8
print("Fruits:", fruit1, fruit2, fruit3)

# 8. Tuple with Different Data Types (टपल में विभिन्न प्रकार के डेटा)
mixed_tuple = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# 9. Nested Tuple (टपल के अंदर टपल)
nested_tuple = ((1, 2, 3), ("A", "B", "C"))
print("Nested Tuple:", nested_tuple)
print("First element of first tuple:", nested_tuple[0][0])  # 1
print("Second element of second tuple:", nested_tuple[1][1])  # B

# 10. Converting List to Tuple (सूची को टपल में बदलना)
list1 = [10, 20, 30, 40]
converted_tuple = tuple(list1)
print("Converted Tuple:", converted_tuple)

# 11. Finding Length of a Tuple (टपल की लंबाई निकालना)
tuple9 = (1, 2, 3, 4, 5)
print("Length of Tuple:", len(tuple9))

# 12. Sorting a Tuple (टपल को सॉर्ट करना - केवल तब संभव जब सभी तत्व समान प्रकार के हों)
tuple10 = (50, 10, 30, 20, 40)
sorted_tuple = tuple(sorted(tuple10))  # sorted() फ़ंक्शन सूची वापस करता है, इसलिए इसे फिर से टपल में बदलना होगा
print("Sorted Tuple:", sorted_tuple)

# 13. Max and Min Values in a Tuple (टपल में अधिकतम और न्यूनतम मान खोजें)
tuple11 = (5, 12, 9, 30, 2)
print("Max value in tuple:", max(tuple11))
print("Min value in tuple:", min(tuple11))

# 14. Converting Tuple to String (टपल को स्ट्रिंग में बदलना)
tuple12 = ('P', 'y', 't', 'h', 'o', 'n')
string_from_tuple = ''.join(tuple12)
print("Tuple as String:", string_from_tuple)

# 15. Iterating Through a Tuple (टपल पर लूप चलाना)
tuple13 = (10, 20, 30, 40, 50)
for item in tuple13:
    print("Tuple Element:", item)

# 16. Checking if Tuple is Empty (टपल खाली है या नहीं)
empty_tuple = ()
print("Is tuple empty?", len(empty_tuple) == 0)

# 17. Deleting a Tuple (टपल को पूरी तरह से हटाना)
delete_tuple = (1, 2, 3)
del delete_tuple  # यह टपल को पूरी तरह से डिलीट कर देगा

#--------------------Set------------------------------------------
"""
4. Set Types (Unordered Collections)
Set types store multiple values but do not maintain any specific order.
4.1 set (Set - Unique Items Collection)
Stores unique values (no duplicates are allowed).
The order of elements is not fixed (unordered).
Supports mathematical operations like union, intersection, and difference.
Used in cases where duplicate values should be removed or when working with distinct groups of items.
* Note: Set items are unchangeable, but you can remove items and add new items.]
To add one item to a set use the add() method.

"""
# Set Methods in Python

# 1. add() - Adds a single element to the set.
my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print("After add:", my_set)

# 2. update() - Adds multiple elements to the set.
my_set.update([5, 6, 7])  # Adds multiple elements
print("After update:", my_set)

# 3. remove() - Removes a specific element; raises an error if not found.
my_set.remove(3)  # Removes 3
print("After remove:", my_set)

# 4. discard() - Removes a specific element; does not raise an error if not found.
my_set.discard(10)  # Does nothing as 10 is not in the set
print("After discard:", my_set)

# 5. pop() - Removes and returns an arbitrary element from the set.
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop:", my_set)

# 6. clear() - Removes all elements from the set.
my_set.clear()
print("After clear:", my_set)

# 7. union() - Returns a new set with all elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# 8. intersection() - Returns a new set with only common elements.
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 9. difference() - Returns a new set with elements only in the first set.
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# 10. symmetric_difference() - Returns elements not common in both sets.
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# 11. issubset() - Checks if one set is a subset of another.
subset_check = {1, 2}.issubset(set1)
print("Is subset:", subset_check)

# 12. issuperset() - Checks if one set is a superset of another.
superset_check = set1.issuperset({1, 2})
print("Is superset:", superset_check)

# 13. isdisjoint() - Checks if two sets have no common elements.
disjoint_check = {8, 9}.isdisjoint(set1)
print("Is disjoint:", disjoint_check)

# 14. copy() - Returns a shallow copy of the set.
copied_set = set1.copy()
print("Copied set:", copied_set)

# -------------------------------------------------
# -----------------Dictionary (dict) Methods-------------------------------------------------
"""
Dictionary (Dict - Key-Value Collection)
एक unordered collection है, जिसमें key-value pairs स्टोर किए जाते हैं।
Keys unique होती हैं और immutable होनी चाहिए (जैसे string, number, tuple)।
Values किसी भी data type की हो सकती हैं।
Dictionary का उपयोग data को key-value pair के रूप में store और manage करने के लिए किया जाता है।
"""

# ============================================
# (A) Accessing Elements (एलिमेंट एक्सेस करना)
# ============================================

a = {"a": 34, 2: 43}

# सभी values प्राप्त करना
print(a.values())  # Output: dict_values([34, 43])

# सभी keys प्राप्त करना
print(a.keys())  # Output: dict_keys(['a', 2])

# Dictionary की लंबाई (keys की संख्या) प्राप्त करना
print(len(a))  # Output: 2

# ============================================
# (B) Adding & Updating Elements (एलिमेंट जोड़ना और अपडेट करना)
# ============================================

# नई key-value जोड़ना
a["newadd"] = 12
print(a)  # Output: {'a': 34, 2: 43, 'newadd': 12}

# मौजूदा key की value अपडेट करना
a.update({2: 44})
print(a)  # Output: {'a': 34, 2: 44, 'newadd': 12}

# नई key-value update() द्वारा जोड़ना
a.update({"newadd": 456})
print(a)  # Output: {'a': 34, 2: 44, 'newadd': 456}

# ============================================
# (C) Removing Elements (एलिमेंट हटाना)
# ============================================

# किसी विशेष key की value हटाना (और return करना)
removed_value = a.pop("a")
print(a)  # Output: {2: 44, 'newadd': 456}
print(removed_value)  # Output: 34

# popitem() अंतिम जोड़ी गई key-value को हटाता है
a.popitem()
print(a)  # Output: {2: 44}

# del का उपयोग करके key-value जोड़ी को हटाना
del a[2]
print(a)  # Output: {}

# clear() का उपयोग करके पूरी dictionary खाली करना
a.clear()
print(a)  # Output: {}

# ============================================
# (D) Searching & Counting (खोज और गिनती)
# ============================================

b = {"apple": 5, "banana": 3, "cherry": 7}

# किसी key की उपस्थिति जांचना
print("apple" in b)  # Output: True
print("grape" in b)  # Output: False

# get() का उपयोग करके सुरक्षित रूप से value प्राप्त करना
print(b.get("banana"))  # Output: 3
print(b.get("grape", "Not Found"))  # Output: Not Found

# count समान keys नहीं होते, लेकिन values की गिनती संभव नहीं है।
# Dictionary में keys की गिनती
print(len(b))  # Output: 3

# ============================================
# (E) Copying Dictionary (डिक्शनरी कॉपी करना)
# ============================================

# copy() shallow copy बनाता है
b_copy = b.copy()
print(b_copy)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}

# deep copy बनाने के लिए deepcopy()
import copy
b_deepcopy = copy.deepcopy(b)
print(b_deepcopy)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}

# ============================================
# (F) Dictionary Comprehension (संक्षिप्त रूप में डिक्शनरी बनाना)
# ============================================

squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ============================================
# (G) Merging Dictionaries (डिक्शनरी को मर्ज करना)
# ============================================

dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}

# update() का उपयोग करके मर्ज करना
dict1.update(dict2)
print(dict1)  # Output: {'x': 1, 'y': 3, 'z': 4}

# ** (unpacking operator) का उपयोग करके मर्ज करना
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'x': 1, 'y': 3, 'z': 4}
