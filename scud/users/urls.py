from django.urls import path
from .views import logout_user, login_user, register, settings

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('settings/', settings, name='settings'),
]



