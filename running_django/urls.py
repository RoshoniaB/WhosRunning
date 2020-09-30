from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('running.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
    path('', include('users.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
