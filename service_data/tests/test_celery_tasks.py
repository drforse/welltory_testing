"""
testing celery tasks
"""
from typing import Optional

import pytest

from service_data.models import UserWeight
from service_data.redis import redis_app
from service_data.celery_tasks import process_user_weight_data
from service_data.serializers import PostUserWeightSerializer


@pytest.mark.django_db
def test_task_cleans_redis(celery_session_worker):
    dt = b'{"day": "2021-05-09", "user_id": 2, "weight": 75.23, "unit": "kg"}'
    redis_app.set("user_weight_data:1", dt)
    assert redis_app.get("user_weight_data:1") == dt
    process_user_weight_data.delay("1").get()
    assert redis_app.get("user_weight_data:1") is None


@pytest.mark.django_db
def test_task_saves_not_even(celery_session_worker):
    dt = b'{"day": "2021-05-09", "user_id": 2, "weight": 75.23, "unit": "kg"}'
    redis_app.set("user_weight_data:1", dt)
    result: Optional[dict] = process_user_weight_data.delay("1").get()
    assert result in PostUserWeightSerializer(UserWeight.objects.all(), many=True).data


@pytest.mark.django_db
def test_task_does_not_save_even(celery_session_worker):
    dt = b'{"day": "2021-05-09", "user_id": 2, "weight": 75.24, "unit": "kg"}'
    redis_app.set("user_weight_data:1", dt)
    result: Optional[dict] = process_user_weight_data.delay("1").get()
    assert result not in PostUserWeightSerializer(UserWeight.objects.all(), many=True).data