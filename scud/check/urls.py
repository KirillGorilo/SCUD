from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('qr-code/', views.generate_qr_code, name='generate_qr_code'),
    path('update_qr/', views.update_id_now, name='update_id'),
    path('find_user/<str:user_id>/', views.find_user, name='find_user'),
]