# ------SQLALCHEMY/Toolkit Object relational mapper that allows us to map py classes and obj to db tables and entries

# ------Translates Obj and Classes to Database tables and entries
# ------We can focus on python objects and the code/no need for SQL
# ------pip install sqlalchemy
# ------
# ------
# ------
# ------
# ------

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR

# ------datatypes fot the columns. Column itself/FK relations of the DB we are going to define
from sqlalchemy.ext.declarative import declarative_base

# ------The baseclass we are going to extend
from sqlalchemy.orm import sessionmaker

# ------The baseclass we inherit from will be created by
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    ssn = Column(
        "ssn", Integer, primary_key=True
    )  # -----person has unique identifier(primary key)/THAT WILL BE A COLUMN. Name it "ssn", integer
    firstname = Column("firstname", String)
    lastname = Column("firstname", String)
    # Pattern is quite simple. 1-provide attributename(ssn, fn, ln) 2-databasename(ssn) Databasetyp, optionalparamenters nullable,
    age = Column("age", Integer)
    gender = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, age, gender):  # ----init constructor
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __repr__(
        self,
    ) -> str:  # ----repr func/ allows us to specify how we want to print a person/what will we see when print
        return (
            f"({self.ssn}){self.firstname} {self.lastname} ({self.age},{self.gender})"
        )


engine = create_engine("sqlite:///mydb.db", echo=True)
# once we have class wecreate an engine and specify the db. Connect to sqlite?Choosing file db/mydb.db/ echo true connects to db
Base.metadata.create_all(
    bind=engine
)  # takes all classes that extend from base and creates them in the db.  Person table will be created now

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12311, "mike", "smith", "m", 35)
session.add(person)
session.commit()

p1 = Person(12312, "anna", "smith", "f", 21)
p2 = Person(12313, "bob", "smith", "m", 35)
p3 = Person(12314, "rocco", "smith", "m", 76)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit
