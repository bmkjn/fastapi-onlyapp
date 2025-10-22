from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI on Azure!"}
 
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}