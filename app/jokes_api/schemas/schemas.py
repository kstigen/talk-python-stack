import abc
from uuid import UUID

from pydantic import BaseModel as PydanticBaseModel, Field, validator


class BaseModel(PydanticBaseModel, abc.ABC):
    class Config:
        orm_mode = True


class Joke(BaseModel):
    """
    A very funny joke
    """
    joke_id: UUID = Field(description="Global identifier for a joke")
    joke_content: str = Field(description="The joke content")
    joke_author: str | None = Field(description="The author of the joke, if known.")

    @validator('joke_content')
    def joke_must_contain_chuck_norris(cls, joke_content):
        if 'Chuck' not in joke_content:
            raise ValueError('The joke must contain Chuck Norris')

        return joke_content

# Viktige punkter
# orm_mode --> Bruker dict-representasjon av objektet til å mappe
