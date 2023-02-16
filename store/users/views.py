from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
# Create your views here.
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title' : 'Авторизация', 'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем, вы успешно зарегестрировались!")
            return HttpResponseRedirect(reverse('users:login'))
        else:
            form = UserRegistrationForm()
    context =  {'title' : 'Регистрация', 'form' : UserRegistrationForm()}
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {'title' : 'Профиль',
               'form' : form,
               'baskets' : Basket.objects.all()}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))