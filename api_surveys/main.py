from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()      



class Users(BaseModel):
    username: str
    email: str


class Surveys(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: int
    # created_at: datetime.datetime
    # updated_at: datetime.datetime

    


@app.get("/")                           
async def root():
    return{"message":"Hello World"}     

@app.get("/surveys")
async def root():
    return{"surveys": "Hello World"}

@app.get("/users")
async def root():
    return{"surveys": "Hello World"}

@app.post("/users/")
async def create_user(user: Users):
    return user

@app.post("/surveys/")
async def create_survey(survey: Surveys):
    return survey