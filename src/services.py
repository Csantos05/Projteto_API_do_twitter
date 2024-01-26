from typing import Any, Dict, List

import tweepy

from src.connection import tweet_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def _get_tweet(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    breakpoint()
    tweet = api.trends_place(woe_id)

    return tweet[0]["tweet"]


def get_tweet_from_mongo() -> List[Dict[str, Any]]:
    tweet = tweet_collection.find({})
    return list(tweet)


def save_tweet() -> None:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    tweet = _get_tweet(woe_id=BRAZIL_WOE_ID, api=api)
    tweet_collection.insert_many(tweet)
