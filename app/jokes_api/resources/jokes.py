from fastapi import APIRouter

router = APIRouter()


@router.get("/jokes", tags=["jokes"])
async def get_jokes():
    return {"all-the-jokes"}


# Viktige punkter:
# async
