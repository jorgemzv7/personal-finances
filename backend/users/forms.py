from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from wallets.models import Currency

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    favorite_currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 