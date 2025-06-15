from django.core.management.base import BaseCommand
from wallets.models import Currency

class Command(BaseCommand):
    help = 'Populate the database with the most common currencies'

    def handle(self, *args, **kwargs):
        currencies = [
            {'code': 'EUR', 'name': 'Euro', 'symbol': '€'},
            {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
            {'code': 'GBP', 'name': 'British Pound', 'symbol': '£'},
            {'code': 'JPY', 'name': 'Japanese Yen', 'symbol': '¥'},
            {'code': 'AUD', 'name': 'Australian Dollar', 'symbol': 'A$'},
            {'code': 'CAD', 'name': 'Canadian Dollar', 'symbol': 'C$'},
            {'code': 'CHF', 'name': 'Swiss Franc', 'symbol': 'Fr'},
            {'code': 'CNY', 'name': 'Chinese Yuan', 'symbol': '¥'},
            {'code': 'INR', 'name': 'Indian Rupee', 'symbol': '₹'},
            {'code': 'BRL', 'name': 'Brazilian Real', 'symbol': 'R$'},
            {'code': 'RUB', 'name': 'Russian Ruble', 'symbol': '₽'},
            {'code': 'BTC', 'name': 'Bitcoin', 'symbol': 'BTC'},
            {'code': 'ETH', 'name': 'Ethereum', 'symbol': 'ETH'},
            {'code': 'XRP', 'name': 'Ripple', 'symbol': 'XRP'},
            {'code': 'SOL', 'name': 'Solana', 'symbol': 'SOL'},
        ]

        for currency_data in currencies:
            currency, created = Currency.objects.get_or_create(
                code=currency_data['code'],
                defaults={
                    'name': currency_data['name'],
                    'symbol': currency_data['symbol']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Currency created: {currency.code} - {currency.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Currency already exists: {currency.code} - {currency.name}')
                ) 