from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)

from rest_framework.viewsets import GenericViewSet


from django.contrib.auth import get_user_model

from .serializers import UserSerializer 


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  GenericViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
