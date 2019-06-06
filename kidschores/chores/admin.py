from django.contrib import admin
from .models import Chores, Profile
# Register your models here.

admin.site.register(Chores),
admin.site.register(Profile)