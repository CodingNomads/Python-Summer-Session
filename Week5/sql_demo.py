# Demo of basic SQL access using SQLAlchemy

from sqlalchemy import create_engine, MetaData, Table, select, insert, update, delete
from sqlalchemy.orm import Session

# First, create an Engine object, which represents a connection
# to the SQL Engine
#
# Substitute your own connection string for the one below
# Details at https://docs.sqlalchemy.org/en/21/tutorial/engine.html
engine = create_engine("mysql+pymysql://dbuser:dbuser@localhost:33060/sakila")

# Next, get the Metadata from the Engine, which allows you to access
# tables using the Object Relational Model (ORM) using Python.
#
# Details at https://docs.sqlalchemy.org/en/21/tutorial/metadata.html
metadata = MetaData()

# With the Metadata object, you can create Table objects, which connect to
# tables in your SQL engine. The autoload_with named parameter tells
# SQLAlchemy to use the named Engine object to automatically load the table
#
# Details at https://docs.sqlalchemy.org/en/21/tutorial/metadata.html
actors = Table("actor", metadata, autoload_with=engine)
users = Table("users", metadata, autoload_with=engine)

# Next, create a Session object, which defines a single SQL transaction consisting of
# SQL statements which are all committed to the database as an atomic unit
# The Session uses the Engine you created above, and, when used in a with block,
# will automatically be destroyed.
#
# You should create a new Session for each specific use context, and not a single
# Session for the life of your application. Each Session is an open resource
# against your database
#
# Details at https://docs.sqlalchemy.org/en/21/tutorial/dbapi_transactions.html#executing-with-an-orm-session

with Session(engine) as session:

    # Within a session, you can perform all major CRUD operations.
    # First, you can SELECT data from your database
    # The Python code below corresponds to following SQL:
    #
    # SELECT actor.actor_id, actor.first_name, actor.last_name, actor.last_update
    # FROM actor
    # WHERE actor.first_name = "BURT"
    #
    # Details at https://docs.sqlalchemy.org/en/21/tutorial/data_select.html

    stmt = select(actors).where(actors.c.first_name == "BURT")

    # Executing this code results in an iterator you can use to access each
    # row of data returned
    for row in session.execute(stmt):
        print(row)

with Session(engine) as session:

    # Next, you can INSERT data into a database table as well
    # The Python code below corresponds to following SQL:
    #
    # INSERT INTO users (name) VALUES ("Monty")
    #
    # Details at https://docs.sqlalchemy.org/en/21/tutorial/data_insert.html

    stmt = insert(users).values(name="Monty")

    # Executing this statement returns a result, which you can inspect to
    # see how many rows were affected
    result = session.execute(stmt)
    print(f"Inserted {result.rowcount} row.")

    # Because this statement alters data in the database, it must be committed
    # to be persisted
    session.commit()


with Session(engine) as session:

    # You can UPDATE data in a database table
    # The Python code below corresponds to following SQL:
    #
    # UPDATE users SET name="Python" WHERE users.name = "Monty"
    #
    # Details at https://docs.sqlalchemy.org/en/21/tutorial/data_update.html

    stmt = update(users).where(users.c.name == "Monty").values(name="Python")

    # Executing this statement also returns a result, which you can inspect to
    # see how many rows were affected
    result = session.execute(stmt)
    print(f"Updated {result.rowcount} row.")

    # Because this statement alters data in the database, it must be committed
    # to be persisted
    session.commit()


with Session(engine) as session:

    # Finally, you can DELETE data from a database table
    # The Python code below corresponds to following SQL:
    #
    # DELETE FROM users WHERE users.name = "Python"
    #
    # Details at https://docs.sqlalchemy.org/en/21/tutorial/data_update.html#the-delete-sql-expression-construct

    stmt = delete(users).where(users.c.name == "Python")

    # Executing this statement also returns a result, which you can inspect to
    # see how many rows were affected
    result = session.execute(stmt)
    print(f"Deleted {result.rowcount} row.")

    # Because this statement alters data in the database, it must be committed
    # to be persisted
    session.commit()
