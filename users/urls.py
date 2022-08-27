from django.urls import path
from users.views import login, register, profile, home

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('paypal/', home, name='home'),
    #path('paypal-return/', views.paypal_return(), name='paypal-return'),
    #path('paypal-cancel/', views.paypal_cancel(), name='paypal-cancel'),
]
