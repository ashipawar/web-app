from django.urls import include, path 
from .viewset import VideoViewSet  
from .routers import router
 

urlpatterns = [
    path('',include(router.urls)),
 ]
