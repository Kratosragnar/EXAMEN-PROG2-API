# Q1 : /hello
@app.get("/hello", status_code=200)
def hello():
    return "Hello world"