from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings


class Chores(models.Model):
    name = models.CharField(max_length=140)
    time_listed = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    pay = models.FloatField()
    image = models.ImageField(blank=True, upload_to='images/')
    completed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    @property
    def expired(self):
        if datetime.now() > self.expire_date:
            return True
        return False
        