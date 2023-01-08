from rest_framework import serializers 
from .models import Video 
#This serializer will allow you to convert your Video models into 
#JSON format, with the id, title, description, and video_file fields included.
class VideoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Video 
        fields = [
            'id','title','description','video_file','thumbnail','category'
        ]