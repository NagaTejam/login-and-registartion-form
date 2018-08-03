from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from core.forms import SignUpForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def view_profile(request):
    args= {'user':request.user}
    return render(request,'profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
            form = EditProfileForm(instance=request.user)
            return render(request, 'edit_profile.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile')
        else:
            return redirect
    else:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'change_password.html', {'form': form})