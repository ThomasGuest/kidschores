from django.db import models


class Chores(models.Model):
    name = models.CharField(max_length=140)
    time_listed = models.DateTimeField(auto_now_add=True)
    expired_listing = models.DateTimeField()
    pay = models.FloatField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name