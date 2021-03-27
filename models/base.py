import MySQLdb
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# sqlite
# db = create_engine('sqlite:///database.db', echo=True)
# session = scoped_session(sessionmaker(autocommit=False,
#                                       autoflush=True,
#                                       bind=engine))

db = MySQLdb.connect(host=os.getenv('host'),
                     user=os.getenv('user'),
                     passwd=os.getenv('passwd'),
                     db=os.getenv('db'))

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=True,
                                      bind=db))

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

Base = declarative_base()
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=db)


init_db()
