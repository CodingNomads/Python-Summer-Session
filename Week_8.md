# Week 8: Decorators & Data Structures

## Why Learn This?

This week deepens your Python fluency:

* **Decorators** help you modify or extend function behavior — great for logging, security, and more.
* **Abstract Data Structures** like stacks and queues teach you how to manage data efficiently.
* You’ll also explore **idiomatic Python**, learning patterns pros use every day.

These topics build the bridge from intermediate to advanced Python, preparing you for technical interviews and large-scale systems.

---

## Concepts & Notes

### Decorators

A decorator is a function that takes another function and extends or modifies its behavior.

**Basic Decorator**

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Decorator with arguments**

```python
def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper

@repeat
def greet(name):
    print(f"Hello, {name}!")

greet("Pythonista")
```

---

### Abstract Data Structures

**Stack (LIFO)**

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2
```

**Queue (FIFO)**

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1
```

**LinkedList (basic custom example)**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n1.next = n2
print(n1.next.data)  # 2
```

---

### Idiomatic Python

* **List Comprehensions**
* **Using `enumerate()`**

```python
for i, value in enumerate(["a", "b", "c"]):
    print(i, value)
```

* **Dictionary Comprehensions**

```python
squares = {x: x**2 for x in range(5)}
```

---

## Quiz – Week 8

1. **What is a decorator?**

2. **What does LIFO stand for?**

3. **Which Python module supports queue structures?**

4. **What keyword is used to apply a decorator?**

5. **True or False: `enumerate()` returns (index, value) pairs.**

6. **What is the result of `[x*2 for x in range(3)]`?**

---

## Coding Challenges – Week 8

### 🔹 Challenge 1: Create a Basic Decorator

**Instructions:**
Write a decorator that prints "Starting..." before and "Done." after the function call.

**Learning Objective:**
Understand how decorators wrap and extend functions.

```python
# TODO: Write a decorator that prints "Starting..." before and "Done." after the function call.

```

---

### Challenge 2: Decorator with Arguments

**Instructions:**
Write a decorator that logs the arguments a function is called with.

**Learning Objective:**
Use `*args` and `**kwargs` in decorators.

```python
# TODO: Write a decorator that logs the arguments a function is called with.

```

---

### Challenge 3: Implement a Stack

**Instructions:**
Use a list to simulate a stack. Push 3 elements, then pop and print each.

**Learning Objective:**
Reinforce stack logic (LIFO).

```python
# TODO: Use a list to simulate a stack. Push 3 elements, then pop and print each.

```

---

### Challenge 4: Implement a Queue

**Instructions:**
Use `deque` to implement a simple queue. Enqueue 3 values, then dequeue all.

**Learning Objective:**
Reinforce queue logic (FIFO).

```python
# TODO: Use `deque` to implement a simple queue. Enqueue 3 values, then dequeue all.

```

---

### Challenge 5: Use `enumerate()` in a Loop

**Instructions:**
Print the index and value of each item in a list using `enumerate()`.

**Learning Objective:**
Write clean, idiomatic loops.

```python
# TODO: Print the index and value of each item in a list using `enumerate()`.

```

---

### Challenge 6: Dictionary Comprehension

**Instructions:**
Create a dictionary where keys are numbers 1-5 and values are their cubes.

**Learning Objective:**
Learn dictionary comprehensions.

```python
# TODO: Create a dictionary where keys are numbers 1-5 and values are their cubes.

```

---

## Week 8 Summary

* You wrote decorators to enhance or modify function behavior.
* You practiced custom data structures like stacks, queues, and linked lists.
* You used idiomatic Python constructs like `enumerate()` and comprehensions.
* You’re now comfortable writing clean, expressive, and reusable code.

These patterns will empower your final capstone project and any advanced Python work.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-301
    * Section 7) Decorators
    * Section 8) Abstract Data Structures
    * Section 9) Idiomatic Data Structures

### Assignments

Complete the following exercises -- you can, of course, do them all:

* 07_decorators
  * 07_01_quote_wrap.py
  * 07_03_text_decoration.py
  * 07_05_decorated_logging.py
* 08_data_structures
  * 08_01_stack.py

Finally, start planning and working on a capstone project for the course. Your final project should demonstrate what you've learned:

* A real-world Python app
* Uses an external API
* Stores data in a SQL database
* Interacts via command-line or simple interface
* Optional: include testing & decorators!

## Additional resource

[Data Structures & Algorithms course](https://codingnomads.com/course/data-structures-algorithms)
