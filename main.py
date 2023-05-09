from fastapi import FastAPI

from app.routers.user_router import router as user_router


app = FastAPI()
app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
