from django.urls import path, include
from .views import index, logout_user, login_user, register, settings

urlpatterns = [
    # path('students/', StudentListView.as_view(), name='students')
    path('home/', index, name='home'),
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('settings/', settings, name='settings'),
]



