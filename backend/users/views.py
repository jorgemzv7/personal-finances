from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('wallets:wallet_list')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automatically after registration
            messages.success(request, 'Account created successfully!')
            return redirect('wallets:wallet_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})