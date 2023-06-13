from fastapi import Depends, Response
from ..service import Service, get_service
from . import router




@router.delete("/shanyraks/{id}", status_code=200)
def delete_tweet(
    id: str,
    svc: Service = Depends(get_service),
):
    svc.repository.delete_tweets_by_id(id=id)

    return Response(status_code=200)