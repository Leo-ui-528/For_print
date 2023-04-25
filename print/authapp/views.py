from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import PrintUserLoginForm, PrintUserRegisterForm, PrintUserEditForm


def login(request):
    login_form = PrintUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('fileupload'))
    context = {
        'login_form': login_form
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def edit(request):

    if request.method == 'POST':
        edit_form = PrintUserEditForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('fileupload'))
    else:
        edit_form = PrintUserEditForm(instance=request.user)

    context = {
        'edit_form': edit_form,
    }

    return render(request, 'authapp/edit.html', context)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = PrintUserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        register_form = PrintUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'authapp/register.html', context)
