from django.shortcuts import render, redirect
from .models import Chores
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


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


def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("chores:home")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request = request,
                template_name = "chores/login.html",
                context={"form":form})

                