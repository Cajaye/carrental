from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Car
from .forms import MyUserForm, CarForm
from django.db.models import Q
from django.contrib import messages
from django.conf import settings


# Create your views here.
def home(request):
    context = {'api_key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, 'home.html',context)


def login_view(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User not found")

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Bad request')

    context = {'page': page}
    return render(request, 'login.html', context)


def register_view(request):
    page = 'register'
    form = MyUserForm()
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # change something if needed
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page, 'form': form, 'api_key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def cars(request):
    q = request.POST.get('q') if request.POST.get('q') is not None else ''
    rentals = Car.objects.filter()
    context = {'rentals': rentals}
    return render(request, 'cars.html', context)


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    cars_owned = user.car_set.all()
    context = {'user': user, 'cars_owned': cars_owned}
    return render(request, 'profile.html', context)
