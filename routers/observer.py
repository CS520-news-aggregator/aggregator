from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from models.observer import Subscriber
from models.data import Message
import requests


observer_router = APIRouter(prefix="/observer")

LIST_OBSERVERS = []


@observer_router.post("/subscribe")
async def add_subscriber(_: Request, subscriber: Subscriber = Body(...)):
    if subscriber in LIST_OBSERVERS:
        raise HTTPException(status_code=400, detail="Observer already subscribed")

    LIST_OBSERVERS.append(subscriber)
    return {"message": "Observer subscribed"}


@observer_router.get("/subscribers")
async def get_subscribers(_: Request):
    return {
        "subscribers": [jsonable_encoder(subscriber) for subscriber in LIST_OBSERVERS]
    }


def update_subscribers(message: str):
    for subscriber in LIST_OBSERVERS:
        print(f"Sending update to {subscriber}")
        url = f"http://{subscriber.ip_address}:{subscriber.port}/subscriber/update"

        try:
            message = Message(post_id=message, message="New post added")
            response = requests.post(url, json=jsonable_encoder(message), timeout=5)
        except requests.exceptions.RequestException:
            print(f"Could not send update to {subscriber}")
            continue

        if response.status_code != 200:
            print(f"Received status code {response.status_code} from {subscriber}")
