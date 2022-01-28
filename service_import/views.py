from urllib.request import urlopen

from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response

from .celery_tasks import import_user_weight


class RunImportTask(views.APIView):
    def get(self, request: Request) -> Response:
        """
        run import task

        1. calls service_api to get fake user weight info
        2. saves data to redis
        3. calls service_data with redis record id (part of redis key)
        """
        import_user_weight.delay()
        return Response(status=status.HTTP_200_OK)
