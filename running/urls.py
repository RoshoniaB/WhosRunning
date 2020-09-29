from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('running/', views.RunningList.as_view(), name='running_list'),
    path('running/<int:pk>', views.RunningDetail.as_view(), name='running_detail'),
]
