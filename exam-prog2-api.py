from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


students_db = []

class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

# Q1 : /hello
@app.get("/hello", status_code=200)
def hello():
    return "Hello world"

# Q2 : /welcome<name> =...
@app.get("/welcome" , status_code=200)
def welcome(name: str):
    return {"message": f"Welcome {name}"}

# Q3 : POST /students
@app.post("/students", status_code=201)
def add_students(new_students: List[Student]):
    students_db.extend(new_students)
    return students_db

# Q4 : GET /students
@app.get("/students")
def get_students():
    return students_db

# Q5 : PUT /students
@app.put("/students")
def update_or_add_student(student: Student):
    for i, stud in enumerate(students_db):
        if stud.Reference == student.Reference:
            students_db[i] = student
            return {"message": "Student updated"}
    students_db.append(student)
    return {"message": "Student added"}



