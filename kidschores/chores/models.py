from django.db import models


class Chores(models.Model):
    name = models.CharField(max_length=140)
    time_listed = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    pay = models.FloatField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    @property
    def is_expired(self):
        if datetime.now > self.expire_date:
            return True
        return False