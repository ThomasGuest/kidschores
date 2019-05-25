from django.shortcuts import render
from .models import Chores


# Create your views here.


def home(request):
    return render(request, 'chores/home.html')


def chore_list(request):
    """Show list of chores"""
    chores = Chores.objects.order_by('name')
    context = {'chores' : chores}
    return render(request, 'chores/chore_list.html', context)