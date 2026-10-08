from fastapi import FastAPI #import class from package
from enum import Enum

app = FastAPI() #create app instance(object) from FastAPI class

@app.get('/') #get method - app home path
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/all')
def get_all_blogs():
    return {'message' : 'All blogs provided'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{typ}')
def blog_type(typ : BlogType):
    return {'message' : f'Blog Type {typ.value}'}


@app.get('/blog/')

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message' : f'Blog with id {id}'}



