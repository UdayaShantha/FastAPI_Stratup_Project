from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel, Field
from uuid import UUID
from typing import List,Annotated
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ChoiseBase(BaseModel):
    choice_txt:str
    is_correct:bool

class QuestionBase(BaseModel):
    question_txt:str
    choices:List[ChoiseBase]

#Connect database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Create end points

db_dependency=Annotated[Session,Depends(get_db)]

@app.post("/questions")
async def create_question(question:QuestionBase,db:db_dependency):
    db_question=models.Question(question_text=question.question_txt)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice=models.Choices(choice_text=choice.choice_txt,is_correct=choice.is_correct,question_id=db_question.id)
        db.add(db_choice)
    db.commit()

@app.get("/get/questions/{question_id}")
async def get_questions(question_id:int,db:db_dependency):
    result=db.query(models.Question).filter(models.Question.id==question_id).first()
    if not result:
        raise HTTPException(status_code=404,detail="Question not found")
    return result


