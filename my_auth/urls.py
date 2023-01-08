from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='registerUser'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]