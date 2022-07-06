# from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import RoomSerializer
from .models import Room
from .permission import IsAuthenticatedOrReadOnly


# without UPDATE (patch, put)
class CRDViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    pass


class RoomViewSet(CRDViewSet):
    queryset = Room.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = super(RoomViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user.pk)
        return queryset
