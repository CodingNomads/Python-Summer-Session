# Week 6: Object-Oriented Programming (OOP)

## Why Learn This?

This week introduces Object-Oriented Programming (OOP) — the foundation of most modern software. OOP helps you:

* Organize code in a scalable, reusable way.
* Build systems that model real-world objects and behaviors.
* Understand the principles behind major frameworks (Flask, Django, SQLAlchemy, etc.)

Mastering OOP is essential for writing maintainable Python code and succeeding in professional software environments.

---

## Concepts & Notes

### Classes & Objects

**Define a class**

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

**Create an object**

```python
fido = Dog("Fido")
fido.bark()  # Fido says woof!
```

---

### Instance Variables & `__init__()`

* `__init__` is the constructor method.
* `self` refers to the instance of the object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### Dunder Methods

“Dunder” = double underscore (e.g., `__str__`, `__repr__`, `__len__`)

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"
```

---

### Inheritance

**Base and Derived Classes**

```python
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

kitty = Cat()
kitty.speak()  # Meow
```

---

### Method Overriding & Composition

* **Overriding**: Redefine methods in a child class.
* **Composition**: Use other classes as part of your class.

```python
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")
```

---

## Quiz – Week 6

1. **What does `__init__()` do in a class?**

2. **What keyword is used to inherit from a parent class?**

3. **What does the `self` keyword represent?**

4. **Which dunder method controls how an object is printed?**

5. **True or False: You can have multiple instances of the same class.**

6. **What is method overriding?**

---

## Coding Challenges – Week 6

### Challenge 1: Create a Class with `__init__`

**Instructions:**
Create a class called `Student` that stores `name` and `grade` and prints them when an instance is created.

**Learning Objective:**
Understand constructors and instance variables.

```python
# TODO: Create a class called `Student` that stores `name` and `grade` and prints them when an instance is created.

```

---

### Challenge 2: Add a Method to the Class

**Instructions:**
Extend your `Student` class with a method that increases the grade.

**Learning Objective:**
Practice adding behavior (methods) to your class.

```python
# TODO: Extend your `Student` class with a method that increases the grade.

```

---

### Challenge 3: Use `__str__` Method

**Instructions:**
Add a `__str__` method to your class so the student prints nicely.

**Learning Objective:**
Use dunder methods to control object representation.

```python
# TODO: Add a `__str__` method to your class so the student prints nicely.

```

---

### Challenge 4: Inheritance and Method Overriding

**Instructions:**
Create a `Teacher` class that inherits from `Person`, but overrides the `introduce()` method.

**Learning Objective:**
Learn basic inheritance and method overriding.

```python
# TODO: Create a `Teacher` class that inherits from `Person`, but overrides the `introduce()` method.

```

---

### Challenge 5: Composition with Engine and Car

**Instructions:**
Create two classes: `Battery` and `Phone`, where `Phone` uses a `Battery`.

**Learning Objective:**
Understand class composition by combining behaviors.

```python
# TODO: Create two classes: `Battery` and `Phone`, where `Phone` uses a `Battery`.

```

---

### Challenge 6: Multiple Objects

**Instructions:**
Create a list of `Dog` objects and make them bark.

**Learning Objective:**
Use multiple instances of a class in a loop.

```python
# TODO: Create a list of `Dog` objects and make them bark.

```

---

## Week 6 Summary

* You learned how to define and instantiate classes.
* You wrote constructors and added methods to encapsulate object behavior.
* You used `__str__` to customize how your objects display.
* You applied inheritance to reuse and override behavior.
* You practiced composition to combine class functionality.

OOP gives you structure and reuse — a critical step toward building larger applications, frameworks, and systems.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-301
    * Section 1) Introduction & Prerequisites
    * Section 2) Classes, Objects, and Methods
    * Section 3) Inheritance

### Assignments

First:
* Install the [Python 301 Lab Exercises](https://codingnomads.com/python-301-download-labs)

Then, complete the following exercises -- you can, of course, do them all:
* 02_classes-objects-methods
  * 02_02_planets.py
  * 02_03_car.py
  * 02_04_classy_shapes.py
  * 02_05_smaller-amount.py
* 03_inheritance
  * 03_01_more_food.py
  * 03_02_inheritance.py
  
