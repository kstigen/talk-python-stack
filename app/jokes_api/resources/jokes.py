from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from jokes_api.dependencies import get_db
from jokes_api.schemas import Joke
from jokes_api.services import joke_service

router = APIRouter()


@router.get(path="/jokes", description="Return all jokes from the api")
def get_jokes(db: Session = Depends(get_db)) -> list[Joke]:
    return joke_service.get_jokes(db)


@router.get(path="/jokes/{joke_id}", description="Get a specific joke")
def get_joke(joke_id: UUID, db: Session = Depends(get_db)) -> Joke:
    the_joke = joke_service.get_joke(db, joke_id)

    if not the_joke:
        raise HTTPException(404, detail=f"Joke with id {joke_id} not found")

    return the_joke


@router.post(path="/jokes", description="Add a joke")
def add_joke(joke: Joke, db: Session = Depends(get_db)) -> Joke:
    try:
        created_joke = joke_service.add_joke(db, joke)
    except Exception:
        db.rollback()
        raise HTTPException(422, detail=f"Could not add joke with id {joke.joke_id}")
    else:
        db.commit()

    return created_joke

# Viktige punkter
# Har fjernet async --> databasedriver støtter ikke async (psycopg3 gjør det) -- har ikke testet den
# Depends --> Dependency injection