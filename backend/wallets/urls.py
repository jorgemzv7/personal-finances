from django.urls import path
from . import views

app_name = 'wallets'

urlpatterns = [
    path('', views.wallet_list, name='wallet_list'),
    path('new/', views.wallet_create, name='wallet_create'),
    path('<uuid:wallet_id>/', views.wallet_detail, name='wallet_detail'),
    path('<uuid:wallet_id>/transactions/new/', views.transaction_create, name='transaction_create'),
] 