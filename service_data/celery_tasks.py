import json
import logging
from typing import Optional

from celery import shared_task

from .redis import redis_app
from .serializers import PostUserWeightSerializer
from .utils import is_even

logger = logging.getLogger(__name__)


@shared_task()
def process_user_weight_data(redis_id: str) -> Optional[dict]:
    redis_key = f"user_weight_data:{redis_id}"
    bdata = redis_app.get(redis_key)
    if bdata is None:
        logger.error(f"no data found under redis_key {redis_key}")
        return None
    redis_app.delete(redis_key)
    data = json.loads(bdata)

    if is_even(data["weight"]) is True:
        return None

    serializer = PostUserWeightSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return serializer.data
