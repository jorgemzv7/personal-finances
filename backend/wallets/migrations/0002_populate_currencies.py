from django.db import migrations

def populate_currencies(apps, schema_editor):
    Currency = apps.get_model('wallets', 'Currency')
    
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
    
    for currency in currencies:
        Currency.objects.get_or_create(
            code=currency['code'],
            defaults={
                'name': currency['name'],
                'symbol': currency['symbol']
            }
        )

def reverse_populate_currencies(apps, schema_editor):
    Currency = apps.get_model('wallets', 'Currency')
    Currency.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_currencies, reverse_populate_currencies),
    ]