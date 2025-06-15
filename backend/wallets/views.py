from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wallet, Transaction
from .forms import WalletForm, TransactionForm

# Create your views here.

@login_required
def wallet_list(request):
    """
    View for listing all wallets for the current user.
    If the user has no wallets, it will redirect to the wallet creation page.
    """
    wallets = Wallet.objects.filter(users=request.user)
    return render(request, 'wallets/wallet_list.html', {'wallets': wallets})

@login_required
def wallet_create(request):
    if request.method == 'POST':
        form = WalletForm(request.POST, user=request.user)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.save()
            wallet.users.add(request.user)  # Añadir el usuario actual como propietario
            messages.success(request, 'Wallet created successfully!')
            return redirect('wallets:wallet_list')
    else:
        form = WalletForm(user=request.user)
    
    return render(request, 'wallets/wallet_form.html', {'form': form})

@login_required
def wallet_detail(request, wallet_id):
    wallet = get_object_or_404(Wallet, id=wallet_id, users=request.user)
    transactions = wallet.transactions.all()
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.wallet = wallet
            transaction.created_by = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('wallets:wallet_detail', wallet_id=wallet.id)
    else:
        form = TransactionForm()
    
    return render(request, 'wallets/wallet_detail.html', {
        'wallet': wallet,
        'transactions': transactions,
        'form': form
    })

@login_required
def transaction_create(request, wallet_id):
    wallet = get_object_or_404(Wallet, id=wallet_id, users=request.user)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.wallet = wallet
            transaction.created_by = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('wallets:wallet_detail', wallet_id=wallet.id)
    else:
        form = TransactionForm()
    
    return render(request, 'wallets/transaction_form.html', {
        'form': form,
        'wallet': wallet
    })
