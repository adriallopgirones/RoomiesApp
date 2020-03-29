from .logic.generate_id import generate_id
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, JoinGroupForm, NewGroupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.apps import apps
import GroupManagerInstance
from shared_list.models import SharedList

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('../../shared_list')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form = form.save(commit=False)
                form.group_id = generate_id()
                form.save()
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
                    if user.is_grouped:
                        new_group_manager(request)
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

def join_group(request):
    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.get(username=request.user)
            if user is not None:
                group_id = form.cleaned_data['group_id']
                user.group_id = group_id
                user.is_grouped = True
                user.save()
                new_group_manager(request)
                return redirect('../../shared_list')
            else:
                print('incorrect')
        else:
            print('incorrect2')

    form = JoinGroupForm()

    return render(request, 'user_system/join_group.html', {"form": form})

def new_group(request):
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sl = SharedList(name=name, group_id=request.user.group_id)
            sl.save()
            User = get_user_model()
            user = User.objects.get(username=request.user)
            user.is_grouped = True
            user.save()
            new_group_manager(request)
            return redirect('../../shared_list')
    else:
            form = NewGroupForm()

    return render(request, 'user_system/new_group.html', {"form": form})

def new_group_manager(request):
    User = get_user_model()
    user = User.objects.get(username=request.user)
    users = User.objects.filter(group_id = user.group_id)
    Purchase = apps.get_model('shared_list', 'Purchase')
    purchases = [Purchase.objects.filter(user=u) for u in users]
    GroupManagerInstance.GM.update_group(users, purchases, user.group_id)


