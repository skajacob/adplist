"""User app urls"""
from django.urls import path, include

urlpatterns = [
    path('user/', include('rest_auth.urls')),
    path('usersinfo/', include('users.routers')),
    path('user/registration/', include('rest_auth.registration.urls')),
]