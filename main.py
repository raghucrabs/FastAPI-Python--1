from fastapi import FastAPI #import class from package

app = FastAPI() #create app instance(object) from FastAPI class

@app.get('/') #get method - app home path
def index():
    return {'message': 'Hello World!'}