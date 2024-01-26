from unittest import mock
from src.services import _get_tweet


def teste_get_tweet():
    mock_api = mock()
    mock_api.trends_place.return_value = []

    _get_tweet(woe_id=1000, api=mock_api)
    assert 1 == 1
