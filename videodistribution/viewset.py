from rest_framework import viewsets 
from .serializer import VideoSerializer 
from .models import Video 
 

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all() 
    serializer_class = VideoSerializer

   