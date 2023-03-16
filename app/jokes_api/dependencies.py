from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://postgres:secret@localhost:5432/postgres" # Denne kunne godt benyttet pydantic settings-management og hentet ting fra env.

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Viktige punkter:
# db.close() skjer etter at responsen fra fast-api er levert
# Bruk yield når man vil kunne gjøre ting etter at man er ferdig å bruke dependencyen.
