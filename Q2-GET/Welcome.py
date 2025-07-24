# Q2 : /welcome<name> =...
@app.get("/welcome" , status_code=200)
def welcome(name: str):
    return {"message": f"Welcome {name}"}