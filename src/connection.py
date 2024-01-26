from pymongo import MongoClient

client = MongoClient("mongodb://dio:dio@localhost:27017/")

db = client.tweet

tweet_collection = db.tweet
