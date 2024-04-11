from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routers.observer import observer_router, update_subscribers

origins = ["*"]


app = FastAPI(title="News Annotator Aggregator", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(observer_router)


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/test-update")
async def test_update():
    update_subscribers("test")
    return {"message": "Test update sent"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True, workers=1)
