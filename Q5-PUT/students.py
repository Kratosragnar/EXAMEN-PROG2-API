# Q5 : PUT /students
@app.put("/students")
def update_or_add_student(student: Student):
    for i, stud in enumerate(students_db):
        if stud.Reference == student.Reference:
            students_db[i] = student
            return {"message": "Student updated"}
    students_db.append(student)
    return {"message": "Student added"}
