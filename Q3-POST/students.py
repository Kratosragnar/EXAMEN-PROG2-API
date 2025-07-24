# Q3 : POST /students
@app.post("/students", status_code=201)
def add_students(new_students: List[Student]):
    students_db.extend(new_students)
    return students_db