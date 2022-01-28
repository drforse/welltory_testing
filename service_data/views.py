from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response

from .celery_tasks import process_user_weight_data
from .models import UserWeight
from .serializers import GetUserWeightSerializer

DEFAULT_GET_LIMIT = 20


class UserWeightView(views.APIView):

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, required=["redis_id"],
        properties={"redis_id": openapi.Schema(type=openapi.TYPE_INTEGER)}
    ))
    def post(self, request: Request) -> Response:
        """
        post a new weight record

        looks for data in redis by key generated from given redis_id,
            then saves the data to db as UserWeight if weight value is even
            (!) and clears data in redis (!)

        data in redis must be json-serialized string

        redis_key is generated like this: f"user_weight_data:{redis_id}"
        """
        redis_id = request.data.get("redis_id")
        if redis_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        process_user_weight_data.delay(redis_id=redis_id)
        return Response(status=status.HTTP_200_OK)


class UserWeightsView(views.APIView):

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter("user_id", in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER,
                          description="filter by user_id",
                          required=True),
        openapi.Parameter("offset", in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER,
                          description="offset results",
                          default=0),
        openapi.Parameter("limit", in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER, 
                          description="limit results",
                          default=20),
    ])
    def get(self, request: Request) -> Response:
        """get weight records for user_id"""
        user_id = request.query_params.get("user_id")
        if user_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        offset = int(request.query_params.get("offset", 0))
        limit = int(request.query_params.get("limit", DEFAULT_GET_LIMIT))

        qs = UserWeight.objects.filter(user_id=user_id).order_by("day").all()[offset:offset + limit]
        user_weights = GetUserWeightSerializer(qs, many=True).data
        return Response(data=user_weights, status=status.HTTP_200_OK)
