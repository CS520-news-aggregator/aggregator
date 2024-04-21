from typing import List
from pydantic import BaseModel


class Post(BaseModel):
    title: str = "Unknown Title"
    link: str = "Unknown Link"
    media: str = "Unknown Media"
    author: str = "Unknown Author"
    date: str = "Unknown Date"

    def __str__(self) -> str:
        return (
            f"{self.title} - {self.link} - {self.media} - {self.author} - {self.date}"
        )


class Message(BaseModel):
    post_ids: List[str]
    message: str
