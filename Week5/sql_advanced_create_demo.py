# Demo of using SQLAlchemy to create and populate tables
# Using the ORM Declarative model (i.e. Python objects which map to SQL)

from typing import List, Optional

from sqlalchemy import (
    String,
    ForeignKey,
    Boolean,
    Column,
    Table,
    create_engine,
    select,
    insert,
    update,
    delete,
)
from sqlalchemy.orm import (
    Session,
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

# First, create an Engine object, which represents a connection
# to the SQL Engine
#
# Substitute your own connection string for the one below
# Details at https://docs.sqlalchemy.org/en/21/tutorial/engine.html
engine = create_engine("mysql+pymysql://dbuser:dbuser@localhost:33060/library")

# Next, get the Metadata from the Engine, which allows you to access
# tables using the Object Relational Model (ORM) using Python.
#
# Details at https://docs.sqlalchemy.org/en/21/tutorial/metadata.html
# metadata = MetaData()


# Now you can start to create tables and relationships between them
# Start by creating a base class as a child of DeclarativeBase
# This class will contain the Metadata object used for all these tables
class Base(DeclarativeBase):
    pass


# Now you can create classes to represent the tables you wish to create
# Here, you will create tables to track books, authors, and genres


# Genre's of books
class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    genre_name: Mapped[str] = mapped_column(String(50))

    # One to Many (one genre for each of many books) relationship
    books: Mapped[List["Book"]] = relationship(back_populates="genre")

    def __str__(self) -> str:
        return f"Genre #{self.id}: {self.genre_name}"


# A pivot for the Many to Many table
books_authors = Table(
    "books_author",
    Base.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("author_id", ForeignKey("authors.id")),
)


# Books
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    loaned: Mapped[bool] = mapped_column(Boolean)

    # Many to One (each book has only one genre) relationship
    genre_id = mapped_column(ForeignKey("genres.id"))
    genre: Mapped["Genre"] = relationship(back_populates="books")

    # Many to Many relationship, using the intermediate table
    authors: Mapped[List["Author"]] = relationship(
        secondary=books_authors, back_populates="books"
    )

    def __str__(self) -> str:
        retval = f"Book #{self.id}: {self.title}"
        if self.loaned:
            retval += ", currently on loan"
        return retval


# Authors
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(80))

    # Many to Many relationship, using the intermediate table
    books: Mapped[List[Book]] = relationship(
        secondary=books_authors, back_populates="authors"
    )

    def __str__(self) -> str:
        return f"Author #{self.id}: {self.first_name} {self.last_name}"


# Next, you can create the link between books and authors
# Because a book can have more than one author, and
# every author can write more than one book, this is
# a separate _pivot_ table, linking each of them.

# books_authors = Table(
#     "books_authors",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("book_id", ForeignKey("books.id"), nullable=False),
#     Column("author_id", ForeignKey("authors.id"), nullable=False),
# )

# Finally, you can create all the tables using the Metadata object
# which is in the Base class
Base.metadata.create_all(engine)

# Now you can add new data to each table
# First, here's some genres to use
with Session(engine) as sess:

    # Example of a bulk edit
    # sess.execute(
    #     insert(Genre),
    #     [
    #         {"genre_name": "History"},
    #         {"genre_name": "Sci-Fi"},
    #         {"genre_name": "Reference"},
    #     ],
    # )

    # Here's an example of defining a Genre for a given book
    genre_hs = Genre(genre_name="History")
    genre_sf = Genre(genre_name="Sci-Fi")
    genre_rf = Genre(genre_name="Reference")
    sess.add(genre_hs)
    sess.add(genre_rf)
    sess.add(genre_sf)

    # Now let's add a few books
    book_bd = Book(title="Braddock's Defeat", loaned=False, genre=genre_hs)
    book_ex = Book(title="Excession", loaned=False, genre=genre_sf)
    book_hg = Book(
        title="Hitchiker's Guide to the Galaxy", loaned=False, genre=genre_sf
    )
    book_dp = Book(title="Design Patterns", loaned=False, genre=genre_rf)
    sess.add(book_bd)
    sess.add(book_ex)
    sess.add(book_hg)
    sess.add(book_dp)

    # Add a few authors
    auth_dp = Author(first_name="David", last_name="Preston")
    auth_ib = Author(first_name="Iain", last_name="Banks")
    auth_da = Author(first_name="Douglas", last_name="Adams")
    auth_eg = Author(first_name="Erich", last_name="Gamma")
    auth_rh = Author(first_name="Richard", last_name="Helm")
    auth_rj = Author(first_name="Ralph", last_name="Johnson")
    auth_jv = Author(first_name="John", last_name="Vlissides")

    sess.add(auth_dp)
    sess.add(auth_ib)
    sess.add(auth_da)
    sess.add(auth_eg)
    sess.add(auth_rh)
    sess.add(auth_rj)
    sess.add(auth_jv)

    # Finally, we can link authors and books
    sess.execute(insert(books_authors).values(book_id=book_bd.id, author_id=auth_dp.id))
    sess.execute(insert(books_authors).values(book_id=book_ex.id, author_id=auth_ib.id))
    sess.execute(insert(books_authors).values(book_id=book_hg.id, author_id=auth_da.id))
    sess.execute(insert(books_authors).values(book_id=book_dp.id, author_id=auth_eg.id))
    sess.execute(insert(books_authors).values(book_id=book_dp.id, author_id=auth_rh.id))
    sess.execute(insert(books_authors).values(book_id=book_dp.id, author_id=auth_rj.id))
    sess.execute(insert(books_authors).values(book_id=book_dp.id, author_id=auth_jv.id))

    # sess.commit()

# Now let's do some querying
# How about looking at all Sci Fi books?
with Session(engine) as sess:

    genre_sf = select(Book).where(Genre.genre_name == "Sci-Fi")
    result = sess.execute(genre_sf)
    for obj in result.scalars():
        print(obj)
