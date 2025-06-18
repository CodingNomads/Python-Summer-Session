# Week 1: Setup, Python Basics, Data Types & Variables

## Why Learn This?

Before building powerful applications with Python, it's essential to understand the fundamentals. Week 1 lays the groundwork for your development journey:

* You’ll set up your tools like a professional developer.
* You’ll write your first Python code and start thinking like a programmer.
* You’ll learn the basic building blocks that every Python program uses.

Whether you're building web apps, analyzing data, or automating tasks, mastering Python basics is a non-negotiable first step.

---

## Concepts & Notes

### Tools of the Trade

**Command Line Interface (CLI)**

```bash
# Check Python version
python --version

# Navigate directories
cd ~/my-folder

# Copy file
cp file_1.txt file_2.txt

# Remove file
rm file_1.txt

# Create a new folder
mkdir new-folder
```

**Git & GitHub**

```bash
# Initialize Git
git init

# Add files and commit
git add <file_name>
git commit -m "Initial commit"
```

**VSCode Tips**

* Install Python extension
* Open Terminal in VSCode (Ctrl+) or (Ctrl`)
* Use IntelliSense for auto-completion - but not too much!
* Do not use any other AI-assist tools while learning

---

### Python Basics

**Hello World**

```python
print("Hello, world!")
```

**Comments**

```python
# This is a comment - it is ignored by the Python interpreter
```

**How Python Thinks**

* Top to bottom, left to right
* Indentation matters (4 spaces, not tabs)
* Readability counts!

---

### Variables & Data Types

**Variables** store values:

```python
name = "Coder"
age = 30
is_student = True
```

**Data Types**

```python
# String
message = "Hello"

# Integer
count = 10

# Float
price = 19.99

# Boolean
is_valid = False
```

**Type Checking**

```python
print(type(name))  # <class 'str'>
```

**Dynamic Typing**
Python doesn't require you to declare variable types ahead of time.

---

## Quiz – Week 1

1. **What command checks your Python version in the CLI?**

2. **What symbol is used for comments in Python?**

3. **What is the data type of: `10.5`?**

4. **What is the output of `type("5")`?**

5. **True or False: Python uses curly braces for blocks of code.**

6. **Which of the following is a valid variable name?**

---

## Coding Challenges – Week 1 

### Challenge 1: Print Your Name

**Instructions:**
Write a Python program that prints your full name to the screen using the `print()` function.

**Learning Objective:**
Practice writing your first line of Python code and get comfortable using the `print()` function to output text.

```python
# TODO: Replace "Coder" with your name
print("My name is Coder")
```

---

### Challenge 2: Create and Print Variables

**Instructions:**
Create two variables: one to store your name, and one to store your age. Then, print both variables in a single line.

**Learning Objective:**
Learn how to declare variables and output multiple values using `print()`.

```python
# TODO: Store your name and age in variables and print them

```

---

### Challenge 3: Calculate Area of a Rectangle

**Instructions:**
Create two variables: `length` and `width`. Assign them numeric values. Calculate the area of the rectangle and print the result.

**Learning Objective:**
Apply mathematical operations to variables and output the result.

```python
# TODO: Change the values and calculate area = length × width

```

---

### Challenge 4: Concatenate Strings

**Instructions:**
Create two variables, `first` and `second`, and assign them string values. Use string concatenation to combine them into one message.

**Learning Objective:**
Understand string manipulation and how to join strings together.

```python
# TODO: Replace with your own words

```

---

### Challenge 5: Use `type()` Function

**Instructions:**
Assign a value to a variable and use the `type()` function to check and print its data type.

**Learning Objective:**
Learn how Python identifies different types of data (e.g., strings, integers, floats, booleans).

```python
# TODO: Try different data types like True, "Hello", 99, 3.14

```

---

### Challenge 6: Use Boolean Logic

**Instructions:**
Create a boolean variable called `is_logged_in` and set it to either `True` or `False`. Then use `print()` to display a message that includes the value of this variable.

**Learning Objective:**
Understand and use boolean data types and simple logic.

```python
# TODO: Set is_logged_in to either True or False

```

---

## Week 1 Summary

* You installed your Python dev tools and learned how to use the CLI, Git, and VSCode.
* You wrote your first Python script and understood how Python executes code.
* You practiced declaring variables and using different data types (strings, numbers, booleans).
* You’ve started thinking like a software engineer by solving small problems programmatically.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-101
    * Section 1) Introduction
    * Section 2) Learn Something New
    * Section 3) Build Something
    * Section 4) Set Up Your Machine
    * Section 5) Introduction to Programming
    * Section 6) Variables and Types

### Assignments

First:
* Create the [Python Folder Structure](https://codingnomads.com/python-101-folder-structure)
* Install the [Python 101 Lab Exercises](https://codingnomads.com/python-101-lab-exercises)

Then, complete the following exercises: (in VSCode)
* 04_build-something -- all exercises
* 05_machine-setup -- all exercises
* 06_intro-to-programming -- all exercises
* 07_variables-and-types -- all exercises
