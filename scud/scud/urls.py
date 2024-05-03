from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('ckeck/', include('check.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
