from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
	name = models.CharField(max_length=45)

	class Meta:
		unique_together = ('user', 'name',)

	def __str__(self):
		return "%s @%s" % (self.name, self.user.username)
