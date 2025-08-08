# import requests
# from bs4 import BeautifulSoup

# URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

# page = requests.get(URL)
# soup = BeautifulSoup(page.text)


# author = soup.find("p", class_="author")
# print(author.text)

# title = soup.find("h1", class_="title")
# print(title.text)

# paragraphs = soup.find_all("li")
# for p in paragraphs:
#     print(p.text)

# try:
#     num = int(input("Enter numerator  : "))
#     den = int(input("Enter denominator: "))
#     # if den == 0:
#     #     raise Exception("Not Chuck Norris")

#     result = num / den
#     print(result)
# except (ValueError, TypeError) as e:
#     print(f"Error '{e}' occurred.")
# except ZeroDivisionError:
#     print("You are not Chuck Norris!")
# finally:
#     print("Finally block")

try:
    x = 10 / 0
finally:
    print("Done")

import unittest


def add(a, b):
    return a + b


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(5, 7), 7)


if __name__ == "__main__":
    unittest.main()

# try:
#     assert add(2, 3) == 5
# except AssertionError as e:
#     print(f"Problem found at {e.args}")
