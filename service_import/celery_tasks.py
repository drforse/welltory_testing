import json
from urllib.request import Request, urlopen

from celery import shared_task
from django.conf import settings

from .redis import redis_app


@shared_task()
def import_user_weight():
    data = urlopen(f"{settings.LOCAL_URL}/service-api/external-fake-api/").read()
    redis_id = _save_to_redis(data)
    send_req = Request(
        f"{settings.LOCAL_URL}/service-data/weight/",
        data=json.dumps({"redis_id": redis_id}).encode(),
        method="POST",
        headers={"Content-Type": "application/json"}
    )
    urlopen(send_req)


def _save_to_redis(data: bytes) -> int:
    """
    takes bytes as data, decodes and saves it to redis under user_weight_data:{id}, returns redis_id
    also increments in redis user_weight_data:id
    """
    redis_id = redis_app.incr("user_weight_data:id", 1)
    redis_app.set(f"user_weight_data:{redis_id}", data.decode("utf-8"))
    return redis_id
