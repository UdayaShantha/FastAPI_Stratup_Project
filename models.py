from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    question_text = Column(String,index=True, nullable=False)

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    choice_text = Column(String,index=True, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))

