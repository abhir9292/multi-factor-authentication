from django.shortcuts import render, redirect
from apps.users.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return redirect('store:home')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            # messages.success(request, f"Welcome {account.get_short_name}. You have successfully logged in.")
            login(request, account)
            return redirect('store:home')
        else:
            messages.error(request, "Error creating account. Please correct the highlighted errors")
    return render(request, "users/register.html", {
        'form': form,
    })

def logout_user(request):
    logout(request)
    return redirect('store:home')