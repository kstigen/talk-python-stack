# workshop-jokes
Repo for talk about fastapi, pydantic, sqlalchemy

## Commands - Step 1
```bash
cd workshop-jokes
poetry init
poetry shell

poetry add fastapi
poetry add uvicorn
```

## Commands - Step 2
```bash
poetry add pydantic

curl localhost:3013/jokes
curl -X POST -H "Content-Type: application/json" -d '{"joke_id": "11595daf-970e-494b-ba11-28bf23a886da", "joke_content": "A joke with Chuck Norris"}' localhost:3013/jokes
```

## Commands - Step 3
```bash
poetry add SQLAlchemy
poetry add psycopg2-binary
poetry add alembic

docker rm -f jokes-db && docker run --name jokes-db -e POSTGRES_PASSWORD=secret -p 5432:5432 postgres:latest

alembic revision -m "Add initial models" --autogenerate
alembic upgrade head

curl localhost:3013/jokes
curl -X POST -H "Content-Type: application/json" -d '{"joke_id": "11595daf-970e-494b-ba11-28bf23a886da", "joke_content": "A joke with Chuck Norris"}' localhost:3013/jokes
```
