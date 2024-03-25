import uvicorn
from fastapi import FastAPI

from routers import product_router

app = FastAPI()


app.include_router(product_router, tags=["Products"])


@app.get("/")
def hello_world():
    return {"message": "Welcome to Fastapi!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
