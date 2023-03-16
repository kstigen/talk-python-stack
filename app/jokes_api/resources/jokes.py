from uuid import uuid4, UUID
from typing import List

from fastapi import APIRouter

from jokes_api.schemas import Joke

router = APIRouter()


@router.get(path="/jokes", response_model=List[Joke], description="Return all jokes from the api")
async def get_jokes():
    return [
        Joke(
            joke_id=uuid4(),
            joke_content="Time waits for no man. Unless that man is Chuck Norris."
        )
    ]


@router.get(path="/jokes/{joke_id}", response_model=Joke, description="Get a specific joke")
async def get_joke(joke_id: UUID):
    return Joke(
        joke_id=joke_id,
        joke_content="Chuck Norris counted to infinity... twice."
    )


@router.post(path="/jokes", response_model=Joke, description="Add a joke")
async def add_joke(joke: Joke):
    return joke
