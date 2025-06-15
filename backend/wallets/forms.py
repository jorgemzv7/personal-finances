from django import forms
from .models import Wallet, Currency, Transaction
from django.utils import timezone

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'currency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Get all currencies
        currencies = Currency.objects.all()
        
        # If the user has a favorite currency, put it first
        if user and user.favorite_currency:
            favorite = user.favorite_currency
            other_currencies = currencies.exclude(id=favorite.id)
            currencies = [favorite] + list(other_currencies)
        
        # Create the options for the select
        self.fields['currency'].queryset = currencies
        self.fields['currency'].empty_label = None  # Don't allow empty selection 

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'transaction_type', 'category', 'notes', 'date']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'value': timezone.now().strftime('%Y-%m-%d')
                }
            ),
        } 