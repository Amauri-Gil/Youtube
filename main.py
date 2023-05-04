from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

myapp = FastAPI()

# Aquí van los métodos GET


@myapp.get('/')
def index():
    return {'data': 'info about the page'}


@myapp.get('/blogs')
def blog_list(limit: int = 10,
              published: bool = True,
              sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@myapp.get('/blog/unpublished')
def unpublished_blogs_list():
    return {'data': 'All unpublished blogs'}


@myapp.get('/blog/unpublished/{id}')
def unpublished_blog(id: int):
    return {'data': id}


@myapp.get('/blog/published')
def published_blogs_list():
    return {'data': 'All published blogs'}


@myapp.get('/blog/published/{id}')
def published_blog(id: int):
    return {'data': id}


@myapp.get('/blog/{id}/comments')
def publishjed_blog_comments(id, limit: int = 10):
    return {'data': {'1', '2'}}


# Aquí van los métodos POST

class Blog(BaseModel):
    title: str
    body: str
    published: bool
    published_at: Optional[str]


@myapp.post('/blog/')
def create_blog(request: Blog):
    return {'data': f'Blog has been created with {request.title} \
            and {request.body}'}
