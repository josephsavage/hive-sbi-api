import logging

from datetime import (datetime,
                      timedelta)
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from django_celery_results.models import TaskResult

from django.http import Http404

from hive_sbi_api.core.models import Member
from .serializers import (UserSerializer,
                          NotFoundSerializer,
                          StatusSerializer,
                          UserInfoHiveSerializer)


logger = logging.getLogger('v0')


class NotFoundResponse:
    def __init__(self, error, status, success=False):
        self.success = success
        self.error = error
        self.status = status


class UserInfoHiveResponse:
    def __init__(self, data, status, success=True):
        self.success = success
        self.data = data
        self.status = status


class StatusResponse:
    def __init__(self, last_updated_time, estimated_minutes_until_next_update, max_sbi_vote):
        self.lastUpdatedTime = last_updated_time
        self.estimatedMinuestUntilNextUpdate = estimated_minutes_until_next_update
        self.maxSBIVote = max_sbi_vote


class UserInfoHiveViewSet(ListModelMixin,
                          RetrieveModelMixin,
                          GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = UserInfoHiveSerializer
    swagger_schema = None
    lookup_field = 'account'

    def get_retrieve_parameter(self, request):
        return request.GET.get('user')

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        user = self.get_retrieve_parameter(self.request)
        filter_kwargs = {self.lookup_field: user}

        obj = self.queryset.filter(**filter_kwargs).first()
        self.check_object_permissions(self.request, obj)

        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        last_sync_task = TaskResult.objects.latest("date_created")
        last_updated_time = last_sync_task.date_created
        next_exec_estimated = last_updated_time + timedelta(hours=2, minutes=24)

        waiting_time = (next_exec_estimated.replace(tzinfo=None) - datetime.now()).total_seconds() / 60

        status_obj = StatusResponse(
            last_updated_time=last_updated_time,
            estimated_minutes_until_next_update=int(waiting_time),
            max_sbi_vote=0,
        )

        status_serializer = StatusSerializer(status_obj)

        if instance:
            data_serializer = self.get_serializer(instance)

            response = UserInfoHiveResponse(
                data=data_serializer.data,
                status=status_serializer.data
            )

            response_serializer = UserSerializer(response)

            return Response(response_serializer.data)

        response = NotFoundResponse(
            error="User doesn't have any shares or doesn't exist.",
            status=status_serializer.data,
        )

        response_serializer = NotFoundSerializer(response)

        return Response(response_serializer.data)

    def list(self, request, *args, **kwargs):
        if self.get_retrieve_parameter(request):
            return self.retrieve(self, request, *args, **kwargs)
        else:
            raise Http404
