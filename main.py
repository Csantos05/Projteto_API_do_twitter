from logging import debug
from typing import List


import uvicorn
from fastapi import FastAPI


from pymongo import MongoClient
from src.responses import TrendItem
from src.services import get_tweet_from_mongo, save_tweet

client = MongoClient("mongodb://localhost:27017")

db = client.tweet

tweet_collection = db.client.teste_tweet_collection


app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_tweet_rote():
    return get_tweet_from_mongo()


if __name__ == "__main__":
    tweet = get_tweet_from_mongo()

if not tweet:
    save_tweet()

uvicorn.run(app, host="0.0.0.0", port=8000)
