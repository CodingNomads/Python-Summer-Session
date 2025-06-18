# Week 5: REST APIs, Databases, Debugging

## Why Learn This?

Week 5 connects Python to the outside world:

* Access real-time data using REST APIs.
* Store and retrieve information from a database using SQLAlchemy.
* Learn debugging strategies to find and fix errors faster.

These are practical, high-leverage skills used in real-world development, from web apps and automation scripts to data pipelines and machine learning systems.

---

## Concepts & Notes

### HTTP & REST APIs

**What is an API?**
An API (Application Programming Interface) allows programs to talk to each other.

**Making a GET request**

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()
print(data["login"])  # octocat
```

**Check response status**

```python
if response.status_code == 200:
    print("Success")
else:
    print("Error:", response.status_code)
```

---

### SQL & SQLAlchemy (Object Relational Mapping - ORM)

**Set up SQL**
Head to [Is MySQL Installed on My Machine](https://codingnomads.com/how-to-install-mysql-add-to-path#how-to-install-mysql) for detailed instructions on how to install MySQL on Linux, Mac, and Windows machines.

**Set up**

Create a new virtual environment and activate it. Then:

```bash
pip install sqlalchemy pymysql cryptography
```

**Basic SQLAlchemy Setup**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('mysql+pymysql://username:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
  
print(actor.columns.keys())
print(repr(metadata.tables['actor']))
```

**Insert Data**

```python
new_user = User(name="Pythonista")
session.add(new_user)
session.commit()
```

**Query Data**

```python
users = session.query(User).all()
for user in users:
    print(user.name)
```

---

### Debugging in Python

**Basic techniques**

```python
print("Checkpoint")  # print debugging

# Use assertions
assert 2 + 2 == 4
```

**Using `pdb`**

```python
import pdb; pdb.set_trace()
```

**Common issues**

* Syntax errors (missing colons, parentheses)
* Runtime errors (division by zero, file not found)
* Logical errors (code runs, but results are wrong)

---

## Quiz – Week 5

1. **Which library is used to make HTTP requests in Python?**

2. **What does `response.json()` return?**

3. **True or False: SQLAlchemy lets you write Python code instead of SQL queries.**

4. **Which function is used to add a new user in SQLAlchemy?**

5. **What does a `status_code` of 404 mean?**

6. **What module lets you step through Python code to debug it?**

---

## Coding Challenges – Week 5

### Challenge 1: Make a Simple API Call

**Instructions:**
Use the `requests` library to get data from a public API (e.g., JSONPlaceholder or GitHub) and print one value.

**Learning Objective:**
Practice retrieving and parsing JSON from a REST API.

```python
# TODO: Use the `requests` library to get data from a public API (e.g., JSONPlaceholder or GitHub) and print one value.

```

---

### Challenge 2: Handle a Failed API Call

**Instructions:**
Modify the above code to check the status code and print an error message if it fails.

**Learning Objective:**
Handle API errors gracefully using conditional logic.

```python
# TODO: Modify the above code to check the status code and print an error message if it fails.

```

---

### Challenge 3: Create a SQLAlchemy Table

**Instructions:**
Define a `Book` class using SQLAlchemy and create the database table.

**Learning Objective:**
Understand how to define models and initialize a database.

```python
# TODO: Define a `Book` class using SQLAlchemy and create the database table.

```

---

### Challenge 4: Add and Retrieve Data with SQLAlchemy

**Instructions:**
Add a new book to your database and print all book titles.

**Learning Objective:**
Insert and query data using SQLAlchemy's session.

```python
# TODO: Add a new book to your database and print all book titles.

```

---

### Challenge 5: Debug a Division Function

**Instructions:**
Add error handling to prevent a division by zero.

**Learning Objective:**
Use `try/except` blocks to catch and handle runtime errors.

```python
# TODO: Add error handling to prevent a division by zero.

```

---

### Challenge 6: Use `pdb` to Inspect Variables

**Instructions:**
Use the `pdb` module to pause execution and inspect variables.

**Learning Objective:**
Step through your code and examine runtime values.

```python
# TODO: Use the `pdb` module to pause execution and inspect variables.

```

---

## Week 5 Summary

* You learned how to retrieve live data from web APIs using the `requests` library.
* You set up a MySQL database and interacted with it through SQLAlchemy ORM.
* You wrote clean database models and queries in Python.
* You improved your debugging skills using `print`, assertions, and `pdb`.

These skills let you build real applications that store data, communicate with external services, and behave reliably.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-201
    * Section 7) APIs and Databases
    * Section 8) Debugging

### Assignments

Complete the following exercises -- you can, of course, do them all:

* Projects
  * barking-shibes.py
* 08_debugging
  * 08_01_revisit_labs.txt
  * 08_02_find_the_bugs.py

Review the [curriculum on SQL](https://codingnomads.com/course/learn-sql-mysql-databases), focusing on [Unit 5: SQL Commands for Querying Databases](https://codingnomads.com/sql-select-statement). This will give you a basic understanding how to use SQL.

Then, using SQLAlchemy and the Sakila database, create the following as separate database queries:

* Select all the actors with the first name of your choice
* Select all the actors and the films they have been in
* Select all the actors that have appeared in a category of a comedy of your choice
* Select all the comedic films and sort them by rental rate
* Using one of the statements above, add a GROUP BY statement of your choice
* Using one of the statements above, add a ORDER BY statement of your choice

You may find it easier to understand these queries by building them in MySQL Workbench first, then writing them in SQLAlchemy. Again, work with your mentor if you are having issues with this.
