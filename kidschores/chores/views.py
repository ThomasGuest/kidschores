from django.shortcuts import render, redirect
from .models import Chores
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login


# Create your views here.


def home(request):
    return render(request, 'chores/home.html')


def chore_list(request):
    """Show list of chores"""
    chores = Chores.objects.order_by('name')
    context = {'chores' : chores}
    return render(request, 'chores/chore_list.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("chores:home")
        
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                        template_name = "chores/register.html",
                        context={"form":form}
            )

    form = UserCreationForm        
    return render(request = request,
                template_name = "chores/register.html",
                context={"form":form})