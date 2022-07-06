from random import randrange
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DeviceSerializer
from .models import Device
from .permission import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from events.models import Event


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


@csrf_exempt
@api_view(['GET'])
def device_values(request, pk):
    # ideal values for temp, co2, humidity respectively
    # 68-76 F, 400-1000 ppm, 30% - 50%
    # generate random values
    temp = randrange(60, 100)
    co2 = randrange(200, 1400)
    humidity = randrange(10, 90)
    device = Device.objects.get(pk=pk)
    values = {'id': pk, 'temp': temp, 'co2': co2, 'humidity': humidity}
    description = "Temp: %sF, CO2: %sppm Humidity: %s%%" % (temp, co2, humidity)
    e = Event(device_id=device, description=description)
    e.save()
    return Response(values)
