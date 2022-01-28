import datetime
import random

from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response


class ExternalFakeApi(views.APIView):
    def get(self, request: Request) -> Response:
        """
        fake api for service_import

        Generate fake values for a user weight record

            day (str): today date in format YYYY-MM-DD
            user_id (int): random integer from 1 to 2147483647
            weight (float): random float from 0.01 to 1500.00 with two decimals 
                (may also give one decimal, see how python round works for more info)
            unit (str): always "kg"
        """
        data = {
            "day": datetime.datetime.now().date(),
            "user_id": random.randint(1, 2147483647),
            "weight": round(random.uniform(0.01, 1500.00), 2),
            "unit": "kg"
        }
        return Response(data=data, status=status.HTTP_200_OK)
