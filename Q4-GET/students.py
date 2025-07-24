# Q4 : GET /students
@app.get("/students")
def get_students():
    return students_db