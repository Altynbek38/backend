from datetime import datetime
from typing import List
from fastapi import HTTPException

from bson.objectid import ObjectId
from pymongo.database import Database


class TweetRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_tweet(self, input: dict):
        payload = {
            "content": input["content"],
            "user_id": ObjectId(input["user_id"]),
            "created_at": datetime.utcnow(),
            "type": input["type"],
            "price": input["price"],
            "address": input["address"],
            "area": input["area"],
            "rooms_count": input["rooms_count"],
            "description": input["description"]
        }

        self.database["tweets"].insert_one(payload)

    def get_tweet_by_user_id(self, user_id: str) -> List[dict]:
        tweets = self.database["tweets"].find(
            {
                "user_id": ObjectId(user_id),
            }
        )
        result = []
        for tweet in tweets:
            result.append(tweet)

        return result
    
    def get_tweet_by_id(self, id: str):
        response = self.database["tweets"].find_one({'_id': ObjectId(id)})
        if response:
            return response
        else:
            raise HTTPException(status_code=404, detail="Element not found")

    def update_tweet(self, id: str, input: dict):
        self.database["tweets"].update_one(
            filter={"_id": ObjectId(id)},
            update={
                "$set": {
                    "content": input["content"],
                    "created_at": datetime.utcnow(),
                    "type": input["type"],
                    "price": input["price"],
                    "address": input["address"],
                    "area": input["area"],
                    "rooms_count": input["rooms_count"],
                    "description": input["description"]
                }
            },
        )
        
    def delete_tweets_by_id(self, id):
        check_exist = self.database["tweets"].find_one({'_id': ObjectId(id)})
        if check_exist:
            self.database["tweets"].delete_one({"_id": ObjectId(id)})
        else:
            raise HTTPException(status_code=404, detail="No permission")