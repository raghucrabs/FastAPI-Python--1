
from fastapi import FastAPI #import class from package
from router import blog_get
from router import blog_post


app = FastAPI() #create app instance(object) from FastAPI class
app.include_router(blog_get.router) #including the blog_get router
app.include_router(blog_post.router) #include the blog_post router

@app.get('/') #get method - app home path
def index():
    return {'message': 'Hello World!'}
