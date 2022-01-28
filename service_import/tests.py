from .celery_tasks import redis_app, _save_to_redis


def test_redis_save():
    data = b'{"day": "2022-01-27", "user_id": 1, "weight": 75.63, "unit": "kg"}'
    redis_id = _save_to_redis(data)
    r_data = redis_app.get(f"user_weight_data:{redis_id}")
    assert r_data == data.decode("utf-8")
