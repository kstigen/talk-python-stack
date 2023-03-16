from uuid import UUID

from pydantic import BaseModel, Field, validator


class Joke(BaseModel):
    """
    A very funny joke
    """
    joke_id: UUID = Field(description="Global identifier for a joke.")
    joke_content: str = Field(description="The joke content.")
    joke_author: str | None = Field(description="The author of the joke, if known.")

    @validator('joke_content')
    def joke_must_contain_chuck_norris(cls, joke_content):  # cls is the class, not the class instance
        if 'Chuck' not in joke_content:
            raise ValueError('The joke must contain Chuck Norris.')

        return joke_content

# Viktige punkter
# * Validering skjer "alle" veier. Både inn og ut
