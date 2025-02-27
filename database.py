from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE= 'postgresql://postgres:Udaya123?@localhost:5432/quizApp_db1'

engine = create_engine(URL_DATABASE)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)