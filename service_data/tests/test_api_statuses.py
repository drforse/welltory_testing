"""
testing api by just http status code in response
"""
import pytest

from rest_framework.test import APIRequestFactory

from service_data.redis import redis_app
from service_data.views import UserWeightView, UserWeightsView


@pytest.mark.django_db
def test_weight_post_200(celery_session_worker):
    dt = b'{"day": "2021-05-09", "user_id": 2, "weight": 75.23, "unit": "kg"}'
    redis_app.set("user_weight_data:1", dt)
    factory = APIRequestFactory()
    request = factory.post("/weight/", {"redis_id": 1}, format="json")
    response = UserWeightView.as_view()(request)
    assert response.status_code == 200


def test_weight_post_400():
    factory = APIRequestFactory()
    request = factory.post("/weight/")
    response = UserWeightView.as_view()(request)
    assert response.status_code == 400


def test_weights_get_400():
    factory = APIRequestFactory()
    request = factory.get("/weights/")
    response = UserWeightsView.as_view()(request)
    assert response.status_code == 400
