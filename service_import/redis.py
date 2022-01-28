from redis import Redis

from django.conf import settings

from fake_redis import FakeRedis

if settings.IS_TEST is False:
    redis_app = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
else:
    redis_app = FakeRedis()  # type: ignore
