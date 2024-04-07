pip install fastapi
pip install uvicorn         # to create a web server

uvicorn main:app --reload   # start up the server

@app.get("/")               # decorador: run function index when calling this path (http://127.0.0.1:8000/)
def index():                
    return("Hello World")

@app.get("/books/{id}")     # input path in URL line: http://127.0.0.1:8000/books/3
def show_books(id: int):
    return{"data": id}   