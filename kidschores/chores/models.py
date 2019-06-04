from django.db import models
import datetime

class Chores(models.Model):
    name = models.CharField(max_length=140)
    time_listed = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    pay = models.FloatField()
    image = models.ImageField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def expired(self):
        if datetime.now() > self.expire_date:
            return True
        return False
        