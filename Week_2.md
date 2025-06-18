# Week 2: Numbers, Math, Text, Loops & User Input

## Why Learn This?

Week 2 expands your Python toolkit with the most used language features in real-world programming:

* Perform calculations and manipulate text.
* Add interactivity through user input.
* Automate repetitive tasks with loops.
* Write conditional logic to build smarter programs.

These skills are foundational for every Python role — from scripting to data science and web development.

---

## Concepts & Notes

### Numbers & Math

```python
# Integers and Floats
x = 10      # int
y = 3.5     # float

# Arithmetic Operators
add = x + y
subtract = x - y
multiply = x * y
divide = x / y
floor_div = x // 3
modulus = x % 3
exponent = x ** 2
```

### Strings & Text

```python
# Concatenation
first = "Hello"
second = "World"
greeting = first + " " + second

# String Indexing
word = "Python"
print(word[0])   # P
print(word[-1])  # n

# Slicing
print(word[0:2])   # Py
print(word[2:])    # thon

# Methods
text = "hello"
print(text.upper())    # HELLO
print(text.capitalize())  # Hello
print(text.replace("l", "y"))  # heyyo
```

### Conditionals

```python
# Booleans & Comparisons
a = 5
b = 10
print(a > b)   # False

# if / elif / else
if a > b:
    print("A is greater")
elif a == b:
    print("Equal")
else:
    print("B is greater")
```

### Loops

```python
# for loop
for i in range(5):
    print("Iteration:", i)

# while loop
x = 0
while x < 3:
    print("x is", x)
    x += 1
```

### User Input

```python
# Input always returns a string
name = input("What is your name? ")
print("Hi", name)

# Convert string to int
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

### Modules and Automation

```python
import random

 # A random number between 0 and 10
print(random.randint(0, 10))
```

```python
# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path('/Users/martin/Desktop')
# Create a new folder
new_path = pathlib.Path('/Users/martin/Desktop/screenshots')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
    # Filter for screenshots only
    if filepath.suffix == '.png':
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)
```

---

## Quiz – Week 2

1. **What data type does `input()` return?**

2. **What is the result of `3 ** 2`?**

3. **What does `print("hello"[1])` output?**

4. **What will this code print?**

   ```python
   x = 10
   if x > 5:
       print("High")
   else:
       print("Low")
   ```

5. **How many times will this loop run?**

   ```python
   for i in range(3):
       print(i)
   ```

6. **True or False: `while` loops must always have a break statement.**

---

## Coding Challenges – Week 2

### Challenge 1: Greet the User

**Instructions:**
Ask the user for their name and print a greeting message.

**Learning Objective:**
Practice using `input()` and string concatenation.

```python
# TODO: Ask the user for their name and print a greeting message.

```

---

### Challenge 2: Simple Calculator

**Instructions:**
Ask the user to input two numbers. Add them and display the result.

**Learning Objective:**
Practice input conversion (`int()` or `float()`) and arithmetic operations.

```python
# TODO: Ask the user to input two numbers. Add them and display the result.

```

---

### Challenge 3: Check Even or Odd

**Instructions:**
Ask the user for a number and tell them whether it is even or odd.

**Learning Objective:**
Use modulus operator `%` and conditional statements.

```python
# TODO: Ask the user for a number and tell them whether it is even or odd.

```

---

### Challenge 4: Word Reverser

**Instructions:**
Ask the user to input a word, then print the word reversed.

**Learning Objective:**
Use string slicing to manipulate text.

```python
# TODO: Ask the user to input a word, then print the word reversed.

```

---

### Challenge 5: Print All Characters of a String

**Instructions:**
Ask for a string and print each character on a new line using a `for` loop.

**Learning Objective:**
Loop through a string and practice iteration.

```python
# TODO: Ask for a string and print each character on a new line using a `for` loop.

```

---

### Challenge 6: Countdown Timer

**Instructions:**
Ask the user for a number and count down to zero using a `while` loop.

**Learning Objective:**
Practice using `while` loops and decrementing values.

```python
# TODO: Ask the user for a number and count down to zero using a `while` loop.

```

---

## Week 2 Summary

* You learned how to work with numbers and math operations in Python.
* You practiced manipulating text and using string methods and slicing.
* You used conditionals to make decisions in your programs.
* You wrote `for` and `while` loops to perform repeated tasks.
* You added interactivity with user input and type conversion.

You're now equipped to build basic interactive programs. These tools will be critical for data processing, logic handling, and user engagement.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-101
    * Section 7) Numbers and Math
    * Section 8) Text and Strings 
    * Section 9) Operators and Booleans
    * Section 10) Conditionals and Loops
    * Section 11) User Input and String Formatting
    * Section 12) Modules and Automation (stretch)

### Assignments (in VSCode)

Complete the following exercises -- you can, of course, do them all:
* 08_numbers-and-math
  * 08_03_seconds_years.py
  * 08_07_convert.py
* 09_strings-and-text
  * 09_01_longest.py
  * 09_02_big_python.py
  * 09_04_sentence_pieces.py
  * 09_08_edibles.py
  * 09_10_file_extensions.py
* 10_operators-and-booleans
  * 10_01_shorthands.py
  * 10_03_temp_converter.py
  * 10_04_modulo_magic.py
  * 10_07_logic_and_booleans.py
* 11_conditionals-and-loops
  * 11_01_decypher_cipher.py
  * 11_04_hunger_meter.py
  * 11_05_squares.py
  * 11_09_primes.py (challenging!)
  * 11_11_fizzbuzz.py
  * 11_13_pig_latinization.py
* 12_user-input-string-formatting
  * 12_01_input_occurrence.py
  * 12_02_input_replace.py
  * 12_06_vowel_counter.py
* 13_modules-and-automation
  * 13_01_math_pi.py
  * 13_02_the_time_please.py
  * 13_03_tech_support_bliss.py
