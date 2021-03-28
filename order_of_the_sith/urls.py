from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', include('recruiting_service.urls'), name = 'recruiting_service'),
    path('test/', include('test_service.urls'), name = 'test_service'),
]
