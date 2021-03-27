from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=True,
                                      bind=engine))


Base = declarative_base()
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
    
init_db()
