import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # ISO 4217 code (e.g., USD, EUR)
    name = models.CharField(max_length=50)  # Full name (e.g., US Dollar, Euro)
    symbol = models.CharField(max_length=5)  # Symbol (e.g., $, €)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name_plural = "Currencies"

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField('users.CustomUser', related_name='wallets')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='wallets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.currency.code})"

    class Meta:
        unique_together = ['name', 'currency']  # A user can't have two wallets with the same name in the same currency

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('TRANSFER', 'Transfer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='EXPENSE')
    date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.wallet.currency.code}"

    class Meta:
        ordering = ['-date']

