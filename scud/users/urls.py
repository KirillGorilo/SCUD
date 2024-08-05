from django.urls import path, include
from .views import logout_user, login_user, register, settings, HelloView
from users import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('login', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('settings/', settings, name='settings'),
    # REST API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/', HelloView.as_view(), name='hello'),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api_token_auth'),

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]



