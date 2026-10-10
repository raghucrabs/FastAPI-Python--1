from typing import Optional
from fastapi import FastAPI #import class from package
from enum import Enum

app = FastAPI() #create app instance(object) from FastAPI class

@app.get('/') #get method - app home path
def index():
    return {'message': 'Hello World!'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message' : 'All blogs provided'}

## Query parameters with default values

# @app.get('/blog/all')
# def get_all_blogs(page=1, page_size=20):
#     return {'message' : f'All {page_size} blogs on page {page}'}

## Optional Parameters

@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int]= None): #optional parameter
    return {'message' : f'All {page_size} blogs on page {page}'}

## Both query and path parameters

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int, comment_id:int, valid:bool = True, username: Optional[str]= None):
    #id and comment_id are path parameters , valid and username are query parameters
    return {'message' : f'blog_id {id}, comment_id {comment_id}, valid{valid}, username {username}'}


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



