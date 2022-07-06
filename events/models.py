from django.db import models
from devices.models import Device
from django.utils import timezone


class Event(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=100)
    occurred_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "Device %s @%s" % (self.device_id, self.occurred_at)

    class Meta:
        ordering = ['-occurred_at']
