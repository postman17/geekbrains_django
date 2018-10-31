from django.shortcuts import render, redirect
from .forms import AccountUserForm, RegisterUserForm
from .models import AccountUser
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

# Create your views here.


def accounts_login(request):
    success_url = reverse_lazy('mainapp:index')
    form = AccountUserForm()
    if request.method == 'POST':
        form = AccountUserForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            usr = authenticate(
                username=user,
                password=pwd
            )
            if usr and usr.is_active:
                login(request, usr)
                return redirect(success_url)

    return render(request, 'accounts/login.html', {'form': form})

def accounts_register(request):
    success_url = reverse_lazy('accounts:login')
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            # Подскажите пожалуйста как правильно проверять наличие записи в базе(без обработчика ошибок)?
            try:
                db_request = AccountUser(username=form.cleaned_data['username'])
            except Exception:
                user = AccountUser(
                    username=form.cleaned_data['username'],
                    is_staff=True,
                    is_superuser=False,
                )
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect(success_url)
            #Почему-то невыводятся ошибки
            form.add_error(None, 'Пользователь существует!')
            return render(request, 'accounts/register.html', {'form': form})

    return render(request, 'accounts/register.html', {'form': form})