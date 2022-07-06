# from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import EventSerializer
from .models import Event


# read-only
class RViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    pass


class EventViewSet(RViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
