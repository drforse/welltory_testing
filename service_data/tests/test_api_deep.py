"""
testing api views deeper than just their http status code
"""
import json
from datetime import date

import pytest
from rest_framework.test import APIRequestFactory

from service_data.models import UserWeight
from service_data.views import UserWeightsView


@pytest.mark.django_db
def test_weights_get():
    UserWeight.objects.create(
        user_id=1,
        day=date(2022, 1, 1),
        weight=50.1
    )
    UserWeight.objects.create(
        user_id=1,
        day=date(2022, 1, 2),
        weight=51.31
    )
    UserWeight.objects.create(
        user_id=2,
        day=date(2022, 1, 1),
        weight=71.33
    )
    UserWeight.objects.create(
        user_id=1,
        day=date(2022, 1, 2),
        weight=51.33
    )
    UserWeight.objects.create(
        user_id=2,
        day=date(2022, 1, 3),
        weight=72.83
    )
    factory = APIRequestFactory()
    request = factory.get("/weights/?user_id=1")
    response = UserWeightsView.as_view()(request)
    results = json.loads(response.rendered_content.decode("utf-8"))
    assert results == [
        {
            "day": "2022-01-01",
            "weight": 50.1
        },
        {
            "day": "2022-01-02",
            "weight": 51.31
        },
        {
            "day": "2022-01-02",
            "weight": 51.33
        }
    ]
