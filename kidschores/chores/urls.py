from django.urls import path
from . import views


app_name = 'chores'
urlpatterns = [
    path('', views.home, name='home'),
    path('chore_list/', views.chore_list, name='chore_list')

]
