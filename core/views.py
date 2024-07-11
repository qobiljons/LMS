from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import UserChangeForm, UserCreateForm

# Create your views here.

def user_create_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


