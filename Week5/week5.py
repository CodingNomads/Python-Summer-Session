#
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, Session
# import sqlalchemy
# from pprint import pprint


# engine = create_engine("mysql+pymysql://dbuser:dbuser@localhost:33060/sakila")
# metadata = sqlalchemy.MetaData()

# users = sqlalchemy.Table("users", metadata, autoload_with=engine)
# stmt = users.insert().values(name="Jon")

# # with engine.connect() as conn:
# #     conn.execute(stmt)
# #     conn.commit()

# stmt = users.insert().values(name="Ryan")

# with engine.connect() as conn:
#     conn.execute(stmt)
#     conn.commit()

# print(stmt)
# import pdb

# pdb.set_trace()


# def add(x, y):
#     return x + y


# print(add(2, 3))
# print(add(4, 19))

import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
pprint(response.json())
