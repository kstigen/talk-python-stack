from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Joke(Base):
    __tablename__ = "joke"
    joke_id = Column(UUID, primary_key=True)
    joke_content = Column(String)
    joke_author = Column(String)
