from fastapi import APIRouter
from typing import Optional,List, Annotated
from fastapi import Query, Body, Path

from pydantic import BaseModel

router = APIRouter(
    prefix= '/blog',
    tags= ['blog']
)

class BlogModel(BaseModel):
    title : str
    content : str
    published : Optional[bool] 


# @router.post('/new')
# def create_blog(blog: BlogModel):
#     return {'data': blog}

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id' : id,
        'data' : blog,
        'version' : version
    }


# Parameter metadata, multiple values for query parameters

@router.post('/new/{id}/comment')
def create_comment(blog:BlogModel, 
                   id:int,
                   comment_id : int = Query(None,
                             title = "Id of the comment",
                             description = "Some description for the comment_id",
                             alias = "commentId",
                             deprecated = True
                             ),
                   content : str = Body(...,
                                        min_length = 10,
                                        max_length = 50,
                                        regex = '^[a-z A-Z]*$'
                                        ),
                    # v: Optional[List[str]] = Query(None)
                    v: Optional[List[str]] = Query(["1.0", '1.1', '1.2'])

                    
                    ):
    return {
        'blog' : blog,
        'id' : id,
        'comment_id' : comment_id,
        'content' : content,
        'version' :v
    }


