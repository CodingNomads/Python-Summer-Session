# Week 3: More Data Types, File I/O, Functions & Scope

## Why Learn This?

This week introduces essential tools that make your programs more powerful and flexible:

* Work with more complex data types like lists and dictionaries.
* Read and write to files for real-world data interaction.
* Create reusable blocks of logic with functions.
* Understand scope — a critical concept for debugging and larger programs.

These skills are essential for data science, backend development, and automation tasks.

---

## Concepts & Notes

### More Data Types

**List**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("date")
print(len(fruits))     # 4
```

**Tuple (immutable list)**

```python
coords = (10, 20)
print(coords[1])       # 20
```

**Set (no duplicates)**

```python
unique_nums = {1, 2, 3, 1}
print(unique_nums)     # {1, 2, 3}
```

**Dictionary (key-value pairs)**

```python
person = {"name": "Coder", "age": 30}
print(person["name"])  # Coder
```

---

### File I/O

**Write to a File**

```python
with open("output.txt", "w") as f:
    f.write("Hello file!")
```

**Read from a File**

```python
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```

---

### Functions & Scope

**Define a Function**

```python
def greet(name):
    return "Hi, " + name

print(greet("Pythonista"))  # Hi, Pythonista
```

**Default Parameters**

```python
def add(x, y=5):
    return x + y

print(add(3))  # 8
```

**Args and Kwargs**

```python
def show_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_args(1, 2, a="apple", b="banana")
```

**Scope**

```python
x = "global"

def my_func():
    x = "local"
    print(x)  # local

my_func()
print(x)      # global
```

---

## Quiz – Week 3

1. **Which data structure is immutable: list, set, tuple, or dict?**

2. **What is the output of `set([1, 2, 2, 3])`?**

3. **How do you write to a file in Python?**

4. **What does `*args` do in a function definition?**

5. **What will this function return?**

   ```python
   def foo(x=1, y=2): return x + y
   print(foo())
   ```

6. **What is the scope of a variable declared inside a function?**

---

## Coding Challenges – Week 3

### Challenge 1: Create a Shopping List

**Instructions:**
Create an empty list, add three items using `.append()`, and print the list.

**Learning Objective:**
Use Python’s list methods to manage a dynamic collection.

```python
# TODO: Create an empty list, add three items using `.append()`, and print the list.

```

---

### Challenge 2: Count Word Frequencies

**Instructions:**
Given a string, count how many times each word appears using a dictionary.

**Learning Objective:**
Learn how to use dictionaries to store frequency counts.

```python
# TODO: Given a string, count how many times each word appears using a dictionary.

```

---

### Challenge 3: Save User Input to File

**Instructions:**
Ask the user for their name and write it to a text file.

**Learning Objective:**
Practice writing to files using Python's `with open()`.

```python
# TODO: Ask the user for their name and write it to a text file.

```

---

### Challenge 4: Read & Print File Contents

**Instructions:**
Open a file and print its contents line by line.

**Learning Objective:**
Reinforce file reading using a context manager.

```python
# TODO: Open a file and print its contents line by line.

```

---

### Challenge 5: Function to Double a Number

**Instructions:**
Write a function `double(x)` that returns `x * 2`.

**Learning Objective:**
Practice defining and calling functions.

```python
# TODO: Write a function `double(x)` that returns `x * 2`.

```

---

### Challenge 6: Print Arguments and Keyword Arguments

**Instructions:**
Write a function that uses `*args` and `**kwargs` and prints them out.

**Learning Objective:**
Understand how to handle variable argument lists in functions.

```python
# TODO: Write a function that uses `*args` and `**kwargs` and prints them out.

```

---

## Week 3 Summary

* You learned about four powerful data types: lists, tuples, sets, and dictionaries.
* You wrote to and read from files — an essential real-world programming skill.
* You defined and called functions to encapsulate reusable logic.
* You learned about scope and how variables behave inside vs. outside functions.
* You saw how to handle any number of inputs with `*args` and `**kwargs`.

These skills allow you to start building real applications, handle structured data, and write modular code.

## For Next Week


### Reading 
* https://codingnomads.com/course/python-programming-201
    * Section 1) Introduction
    * Section 2) More Data Types
    * Section 3) File Input/Output
    * Section 4) Functions and Scope

### Assignments

First:
* Install the [Python 201 Lab Exercises](https://codingnomads.com/python-201-download-labs-project)

Then, complete the following exercises -- you can, of course, do them all:
* 02_more_datatypes
  * 02_02_product_largest.py
  * 02_06_tupled_words.py
  * 02_10_pairing_tuples.py (challenging)
  * 02_12_add_or_not.py
  * 02_14_char_count_dict.py
  * 02_16_inspiring_quotes.py
  * 02_19_comprehension_syntax.py
* 03_file-input-output
  * 03_01_long_words.py
  * 03_03_writing.py
* 04_functions-and-scopes
  * 04_02_mind_the_order.py
  * 04_03_write_letter.py
  * 04_05_docstring_me.py
  * 04_07_determine_divisible.py
  * 04_08_calculate_stats.py
