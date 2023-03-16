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
