from rest_framework import routers  
from .viewset import VideoViewSet

router = routers.DefaultRouter() 
router.register(r'videos',VideoViewSet) 