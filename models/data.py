from pydantic import BaseModel


class Post(BaseModel):
    title: str
    link: str
    media: str
    author: str
    date: str


class Message(BaseModel):
    post_id: str
    message: str
