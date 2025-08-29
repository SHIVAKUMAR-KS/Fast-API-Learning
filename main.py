from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

@app.get("/about")
def about():
    return "This is about us page"
@app.get("/contact")
def about():
    return "This is contact us page"