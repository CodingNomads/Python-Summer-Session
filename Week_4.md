# Week 4: venv, Libraries, List Comprehensions, Lambdas

## Why Learn This?

Week 4 focuses on Python tooling and efficient coding techniques:

* Use libraries to tap into powerful tools without reinventing the wheel.
* Manage dependencies using virtual environments.
* Write cleaner, more expressive code with list comprehensions and lambdas.
* Understand namespaces and error handling.

These are must-have skills for any modern Python developer working in real-world projects, data science, or APIs.

---

## Concepts & Notes

### Virtual Environments

Create an isolated Python environment for your project:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

# Install packages
pip install requests
```

Deactivate:

```bash
deactivate
```

---

### Libraries, Packages & Modules

**Install a library**

```bash
pip install numpy
```

**Importing libraries**

```python
import math
from math import sqrt
import requests
```

**Using modules**

```python
import my_module  # Custom .py file in the same directory
```

---

### List Comprehensions

**Basic Example**

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

**With condition**

```python
evens = [x for x in range(10) if x % 2 == 0]
```

**Nested**

```python
pairs = [(x, y) for x in range(2) for y in range(2)]
```

---

### Lambda Functions

**Quick anonymous functions**

```python
double = lambda x: x * 2
print(double(4))  # 8

add = lambda x, y: x + y
```

**Used with `map()` and `filter()`**

```python
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

---

### Import Namespaces & Errors

**Namespace**
Each file has its own namespace. Avoid `from module import *`.

**Error Handling**

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup")
```

---

## Quiz – Week 4

1. **What is a virtual environment used for?**

2. **Which command activates a virtual environment on macOS/Linux?**

3. **What does this return: `[x for x in range(5) if x % 2 == 1]`?**

4. **What is the output of `lambda x: x * 3` when called with `2`?**

5. **True or False: List comprehensions are faster than for-loops.**

6. **Which package manager is used to install Python libraries?**

---

## Coding Challenges – Week 4 (With Instructions)

### Challenge 1: Create and Use a Virtual Environment

**Instructions:**
Create a virtual environment named `venv`, activate it, and install the `requests` library.

**Learning Objective:**
Learn to isolate your Python environment using `venv`.

```bash
# TODO: Create a virtual environment named `venv`, activate it, and install the `requests` library.

```

---

### Challenge 2: Use a Library Function

**Instructions:**
Import the `math` module and use it to calculate the square root of 81.

**Learning Objective:**
Practice importing and using standard library functions.

```python
# TODO: Import the `math` module and use it to calculate the square root of 81.

```

---

### Challenge 3: Write a List Comprehension

**Instructions:**
Create a list of the squares of numbers from 0 to 9 using list comprehension.

**Learning Objective:**
Write expressive one-liners using list comprehension.

```python
# TODO: Create a list of the squares of numbers from 0 to 9 using list comprehension.

```

---

### Challenge 4: Filter Even Numbers

**Instructions:**
Use `filter()` and a lambda function to return only even numbers from a list.

**Learning Objective:**
Learn how to use functional tools to process data.

```python
# TODO: Use `filter()` and a lambda function to return only even numbers from a list.

```

---

### Challenge 5: Add Error Handling

**Instructions:**
Write a function that divides two numbers, and handles division by zero.

**Learning Objective:**
Introduce `try`/`except` for robust code.

```python
# TODO: Write a function that divides two numbers, and handles division by zero.

```

---

### Challenge 6: Use `map()` with Lambda

**Instructions:**
Use `map()` and `lambda` to triple each number in a list.

**Learning Objective:**
Understand how `map()` works with lambda for transforming data.

```python
# TODO: Use `map()` and `lambda` to triple each number in a list.

```

---

## Week 4 Summary

* You used `venv` to manage project-specific dependencies.
* You installed and imported libraries to access pre-written functionality.
* You wrote more concise Python code using list comprehensions and lambdas.
* You saw how functional programming tools like `map()` and `filter()` simplify data processing.
* You began handling errors gracefully with `try`/`except`.

These skills streamline your coding and are prerequisites for working with APIs, data pipelines, and advanced Python libraries.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-201
    * Section 5) Virtual Environments and Packages
    * Section 6) Advanced Python Concepts

### Assignments


Complete the following exercises -- you can, of course, do them all:
* 05_venvs-and-packages - All exercises
* 06_advanced-python-concepts
  * 06_01_import_this.py
  * 06_04_one_liner.py
  * 06_06_shirt_shop.py
  * 06_08_based_dictcomp.py (challenging)
  * 06_10_divisible_generator.py
  * 06_12_lambda_sum.py
  * 06_15_baby_names.py

### Preparation

To prepare for next week's lessons, please do the following:
* Head to [How to Install MySQL](https://codingnomads.com/how-to-install-mysql-add-to-path#how-to-install-mysql) for instructions on installing MySQL for Linux, Mac, and Windows machines.
* Then, head to [Installing the Sakila Database](https://codingnomads.com/how-to-use-the-sakila-database-in-mysql) to load a sample database we'll use in examples and exercises.

Work with your mentor as necessary to make sure MySQL and the Sakila database is setup properly.
