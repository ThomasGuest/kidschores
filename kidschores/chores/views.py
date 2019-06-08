from django.shortcuts import render, redirect
from .models import Chores, Profile
from .forms import ChoreForm, CompleteForm, ApproveForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    return render(request, 'chores/home.html')

    # TODO: Filter Objects by expired
def chore_list(request):
    """Show list of chores"""
    
    chores = Chores.objects.order_by('name').exclude(completed=True)

    context = {'chores' : chores}
    return render(request, 'chores/chore_list.html', context)

def new_chore(request):
    """admin user creates new available chore"""
    if request.method != 'POST':
        # Create blank form
        form = ChoreForm()
    else:
        # Post data submitted, process data
        form = ChoreForm(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('chores:chore_list'))

    context ={'form' : form}
    return render(request, 'chores/new_chore.html', context)

@login_required
def edit_chore(request, chores_id):
    """User edits available chore"""
    chore = Chores.objects.get(id=chores_id)
    exp = chore.expire_date
    pay = chore.pay
    
    if request.user.get_username() == 'admin':
        if request.method != "POST":
            # Initial request, prefill form with current chore
            form = ChoreForm(instance=chore)
        else:
            # POST data submitted; process data
            form = ChoreForm(instance=chore, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('chores:chore_list'))
    else:
        if request.method != "POST":
            # Initial request, prefill form with current chore
            form = CompleteForm(instance=chore)
        else:
            # POST data submitted; process data
            form = CompleteForm(instance=chore, data=request.POST, files=request.FILES)
            if form.is_valid():
                new = form.save(commit=False)
                new.image = request.FILES.get('image')
                new.owner = request.user
                new.save()
                #form.save()
                return HttpResponseRedirect(reverse('chores:chore_list'))

    context = {'chore': chore, 'form':form, 'exp' : exp, 'pay' : pay}
    return render(request, 'chores/edit_chore.html', context)


def pending_chores(request):
    """list pending chores waitning for approval"""
    chores = Chores.objects.order_by('name').filter(completed=True).exclude(approved=True)
    
    context = {'chores' : chores}
    return render(request, 'chores/pending_chores.html', context)

def approve_chores(request, chores_id):
    chore = Chores.objects.get(id=chores_id)
    pay = chore.pay
    

    if request.method != "POST":
            # Initial request, prefill form with current chore
        form = ApproveForm(instance=chore)
    else:
            # POST data submitted; process data
        form = ApproveForm(instance=chore, data=request.POST)
        if form.is_valid():
            approval = form.save(commit=False)
            chore.owner.profile.deposit(pay)
            approval.save()
            return HttpResponseRedirect(reverse('chores:pending_chores'))

    context = {'chore':chore, 'form':form}
    return render(request, 'chores/approve_chore.html', context)

@login_required
def profile(request):

    return render(request, 'chores/profile.html')
    

# -------Below is User Views, Login, Logout, Register --------

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



#below is for index.html reference for styling

def index(request):
    return render('chores/index.html')