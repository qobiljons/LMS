from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . forms import UserUpdateForm, UserCreateForm
from . models import CustomUser

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


@login_required
def user(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'profile/profile.html', context={"profile":user})


@login_required
def user_edit(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=form.cleaned_data['username'])
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'profile/profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


