from uuid import uuid4, UUID

from fastapi import APIRouter

from jokes_api.schemas import Joke

router = APIRouter()


@router.get(path="/jokes", description="Return all jokes from the api")
async def get_jokes() -> list[Joke]:
    return [
        Joke(
            joke_id=uuid4(),
            joke_content="Time waits for no man. Unless that man is Chuck Norris.",
            joke_author="Chuck Norris"
        )
    ]


@router.get(path="/jokes/{joke_id}", description="Get a specific joke")
async def get_joke(joke_id: UUID) -> Joke:
    return Joke(
        joke_id=joke_id,
        joke_content="Chuck Norris counted to infinity... twice.",
        joke_author="Chuck Norris"
    )


@router.post(path="/jokes", description="Add a joke")
async def add_joke(joke: Joke) -> Joke:
    return joke

# Viktige punkter
# response_model utledes fra type-hintet i funksjonen
