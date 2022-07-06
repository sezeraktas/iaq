from django.db import models
from rooms.models import Room


class Device(models.Model):
	room = models.OneToOneField(
		Room,
		on_delete=models.CASCADE,
		unique=True,
	)
	temp_ideal_value = models.IntegerField(default=70)  # 68-76 F
	co2_ideal_value = models.IntegerField(default=600)  # 400-1000 ppm
	humidity_ideal_value = models.IntegerField(default=40)  # 30% - 50%

	def __str__(self):
		return "Device %s @Room: %s" % (self.pk, self.room.name)
