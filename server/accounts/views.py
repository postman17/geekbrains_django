from django.shortcuts import render, redirect
from accounts.forms import AccountUserForm
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
