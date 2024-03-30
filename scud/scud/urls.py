from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('check.urls')),
    path('admin/', admin.site.urls),
]
