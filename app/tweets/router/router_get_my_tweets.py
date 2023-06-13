from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetMyTweetsTweet(AppModel):
    id: Any = Field(alias="_id")
    content: str


class GetMyTweetsResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: Any = Field(alias="user_id")


@router.get("/shanyraks/{id}", status_code=200, response_model=GetMyTweetsResponse)
def get_my_tweets(id: str, svc: Service = Depends(get_service)) -> dict[str, Any]:
    response = svc.repository.get_tweet_by_id(id)
    return response

