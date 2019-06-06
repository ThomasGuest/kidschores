from django.urls import path
from . import views


app_name = 'chores'

urlpatterns = [
    path('', views.home, name='home'),
    path('chore_list/', views.chore_list, name='chore_list'),
    path('register/', views.register, name='register'),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name='login'),
    path("edit_chore/<int:chores_id>/", views.edit_chore, name="edit_chore"),
    path("new_chore/", views.new_chore, name="new_chore"),
    path("pending_chores/", views.pending_chores, name='pending_chores'),
    path("approve_chores/<int:chores_id>/", views.approve_chores, name='approve_chores'),
    path("profile/", views.profile, name="profile"),

]
