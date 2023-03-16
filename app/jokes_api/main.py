from fastapi import FastAPI

from jokes_api.resources import jokes


def get_app():
    api = FastAPI(title="Jokes API", version="0.0.1")

    api.include_router(jokes.router)
    return api


app = get_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("jokes_api.main:app", host="0.0.0.0", port=3013)
