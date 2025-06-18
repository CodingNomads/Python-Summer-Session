# Week 9: Capstone Project – Python + SQL + APIs Application

## Why Learn This?

This week brings together everything you’ve learned to build a **complete, real-world Python application**. You’ll integrate:

* A command-line interface
* External API data
* SQL database storage using SQLAlchemy
* Functional and object-oriented Python
* Error handling, testing, and file I/O

Building and showcasing a project is essential for:

* Cementing your knowledge
* Demonstrating your skills to employers
* Gaining confidence as a developer

---

## Capstone Project Instructions

### Objective

Build a CLI application that:

* Accepts user input
* Fetches data from a public API
* Saves data to a database (SQLite via SQLAlchemy)
* Displays or modifies stored data
* Includes at least one class and one function

---

### Suggested Project Ideas

1. **Weather Dashboard**

   * Input: City name
   * API: OpenWeatherMap
   * Output: Current weather
   * Store past searches in SQLite

2. **Crypto Tracker**

   * Input: Cryptocurrency symbol
   * API: CoinGecko
   * Output: Current price
   * Log prices over time

3. **Book Search & Save**

   * Input: Book title
   * API: Google Books
   * Output: Book details
   * Save favorites to database

4. **Movie Explorer**

   * Input: Movie title
   * API: OMDB
   * Output: Summary & ratings
   * Add movies to a “watchlist”

---

### Requirements Checklist

| Feature                             | Required |
| ----------------------------------- | -------- |
| Accept user input (CLI)             | ✅        |
| Use an external API (requests)      | ✅        |
| Handle API errors gracefully        | ✅        |
| Use SQLAlchemy for persistence      | ✅        |
| Implement at least one class        | ✅        |
| Include at least one function       | ✅        |
| Use a virtual environment           | ✅        |
| Add a `README.md` with instructions | ✅        |
| Bonus: Add unit tests               | 🔘       |

---

## Example Code Snippet (Weather CLI)

```python
import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine("sqlite:///weather.db")
Session = sessionmaker(bind=engine)
session = Session()

class CityWeather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temp = Column(String)

Base.metadata.create_all(engine)

def get_weather(city):
    try:
        api_key = "your_api_key_here"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        session.add(CityWeather(city=city, temp=str(temp)))
        session.commit()
        print(f"{city.title()} is {temp}°C")
    except Exception as e:
        print("Error:", e)

city = input("Enter a city: ")
get_weather(city)
```

---

## Packaging & Sharing

1. Save your project in a folder:

   * `main.py` (entry point)
   * `requirements.txt`
   * `README.md`
   * Optional: `test_main.py`

2. Run `pip freeze > requirements.txt`

3. Zip or push to GitHub

4. Prepare to demo your project in a 5-minute walkthrough:

   * What it does
   * How it works
   * What tools you used
   * What you learned

---

## Week 9 Summary

* You built a real, working Python app from scratch.
* You connected code to the outside world using APIs and databases.
* You used everything from functions and classes to requests and SQLAlchemy.
* You now have a polished project to showcase on your resume and GitHub.

---

## Graduation Checklist

* [ ] Project Complete and Runs Without Errors
* [ ] Code is Pushed to GitHub
* [ ] README with Setup Instructions
* [ ] You’ve Practiced a Short Demo
* [ ] Certificate Claimed
* [ ] Feedback Submitted
* [ ] You’re Proud of What You Built
