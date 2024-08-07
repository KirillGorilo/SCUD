from django.urls import path, include
from .views import logout_user, login_user, register, settings
from users import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('settings/', settings, name='settings'),
    # REST API
    path('api/users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),


    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]



