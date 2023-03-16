import logging
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from jokes_api import schemas
from jokes_api.models import models


def get_jokes(db: Session) -> list[models.Joke]:
    return list(
        db.execute(
            select(models.Joke)
        ).scalars().all())


def get_joke(db: Session, joke_id: UUID) -> models.Joke | None:
    stmt = (
        select(models.Joke)
        .where(models.Joke.joke_id == joke_id)
    )
    return db.execute(stmt).scalar()


def add_joke(db: Session, joke: schemas.Joke) -> models.Joke:
    db_joke = models.Joke(**joke.dict())
    db.add(db_joke)

    try:
        db.flush()
    except IntegrityError as ie:
        logging.exception(f"Failed to add joke with id {joke.joke_id}")
        raise ie

    return db_joke
