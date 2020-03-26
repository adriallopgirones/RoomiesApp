from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('../../shared_list')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('../../shared_list')
                else:
                    print('incorrect')

            return redirect('.')
        else:
            form = SignUpForm()

        return render(request, 'user_system/signup.html', {"form" : form})


def login_request(request):
    if request.user.is_authenticated:
        return redirect('../../shared_list')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('../../shared_list')
                else:
                    print('incorrect')
            else:
                print('incorrect2')
        form = AuthenticationForm()

        return render(request, 'user_system/login.html', {"form" : form})

def logout_request(request):
    logout(request)
    return redirect('../login')