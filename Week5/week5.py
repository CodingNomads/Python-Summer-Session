#
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import sqlalchemy
from pprint import pprint


engine = create_engine("mysql+pymysql://dbuser:dbuser@localhost:33060/sakila")
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
stmt = users.insert().values(name="Jon")

# with engine.connect() as conn:
#     conn.execute(stmt)
#     conn.commit()

stmt = users.insert().values(name="Ryan")

# with engine.connect() as conn:
#     conn.execute(stmt)
#     conn.commit()

print(stmt)

assert 2 + 2 == 5
