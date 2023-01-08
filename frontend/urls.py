from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='homeView'),
    path('register',views.registerView,name='registerView'),
    path('login',views.loginView,name='loginView'),
    path('logout',views.logoutView,name='logoutView'),
    path('watch/<int:id>/', views.watchView, name='watchView'),
    path('creator',views.creatorView,name='creatorView'),
    path('create',views.createView,name='createView'),
    path('delete',views.deleteView,name='deleteView')
]
