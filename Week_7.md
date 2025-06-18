# Week 7: Web Scraping, Exception Handling & Testing

## Why Learn This?

Week 7 adds powerful capabilities to your Python toolkit:

* **Web Scraping** helps you extract data from the internet.
* **Exception Handling** keeps your programs from crashing.
* **Testing** ensures your code works reliably, even as it grows.

These skills make your code robust and capable of interacting with the real world, and they are essential for data professionals, backend engineers, and automation developers.

---

## Concepts & Notes

### Web Scraping with BeautifulSoup

**Install dependencies**

```bash
pip install requests beautifulsoup4
```

**Basic Scraper**

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string
print("Title:", title)
```

**Finding elements**

```python
# Find all paragraph tags
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
```

---

### Exceptions & Graceful Failure

**Basic Try/Except**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Catching multiple errors**

```python
try:
    x = int("hello")
except (ValueError, TypeError) as e:
    print("Error occurred:", e)
```

**Finally Block**

```python
try:
    print("Try block")
finally:
    print("Always runs")
```

---

### Testing & Test-Driven Development (TDD)

**Basic `assert`**

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

**Using `unittest`**

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 3, 5)

if __name__ == '__main__':
    unittest.main()
```

---

## Quiz – Week 7

1. **Which Python library helps parse HTML for web scraping?**

2. **True or False: `try` blocks must always be followed by `except`.**

3. **What does `soup.find_all("p")` do?**

4. **What Python built-in helps test expected results?**

5. **What is a test case?**

6. **What does the `finally` block do?**

---

## Coding Challenges – Week 7

### Challenge 1: Scrape a Page Title

**Instructions:**
Use `requests` and `BeautifulSoup` to retrieve the title of a web page (e.g., [https://example.com](https://example.com)).

**Learning Objective:**
Perform a basic web scraping task and extract page metadata.

```python
# TODO: Use `requests` and `BeautifulSoup` to retrieve the title of 
# a web page (e.g., [https://example.com](https://example.com)).

```

---

### Challenge 2: Extract All Links

**Instructions:**
Scrape and print all hyperlinks (`<a href>`) from the page.

**Learning Objective:**
Extract attributes using `.get()` in BeautifulSoup.

```python
# TODO: Scrape and print all hyperlinks (`<a href>`) from the page.

```

---

### Challenge 3: Handle an Invalid URL

**Instructions:**
Add error handling for failed HTTP requests (e.g., 404 or wrong URL).

**Learning Objective:**
Combine web scraping with exception handling.

```python
# TODO: Add error handling for failed HTTP requests (e.g., 404 or wrong URL).

```

---

### Challenge 4: Use Try/Except to Catch Conversion Error

**Instructions:**
Convert a string to an integer and catch `ValueError`.

**Learning Objective:**
Safely handle user input or type errors.

```python
# TODO: Convert a string to an integer and catch `ValueError`.

```

---

### Challenge 5: Write a Simple Test Case with `assert`

**Instructions:**
Write a function and test it with an `assert` statement.

**Learning Objective:**
Understand the basics of TDD.

```python
# TODO: Write a function and test it with an `assert` statement.

```

---

### Challenge 6: Use `unittest` for Function Testing

**Instructions:**
Write a test suite for a custom `square()` function using `unittest`.

**Learning Objective:**
Write organized, automated tests for functions.

```python
# TODO: Write a test suite for a custom `square()` function using `unittest`.

```

---

## Week 7 Summary

* You used BeautifulSoup to extract data from real web pages.
* You learned how to prevent program crashes with `try`/`except`.
* You added testing to validate code logic and ensure correctness.
* You wrote unit tests with `unittest` and practiced TDD principles.

These skills are critical for building stable applications and automating real-world workflows.

## For Next Week

### Reading 
* https://codingnomads.com/course/python-programming-301
    * Section 4) Web Scraping
    * Section 5) Exceptions
    * Section 6) Testing

### Assignments

Complete the following exercises -- you can, of course, do them all:

* 04_web-scraping
  * 04_01_get_cn_html.py
  * 04_03_poke_info.py
  * 
* 05_exceptions
  * 05_02_calculator.py
  * 05_04_else_database.py
  * 05_07_find_a_prince.py
* 06_testing
  * 06_02_mymath-tester
  * 06_04_tdd_approach.py
  * 06_05_revisit_testing.py
  
