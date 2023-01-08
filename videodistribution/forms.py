from django import forms
from .serializer import VideoSerializer

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoSerializer.Meta.model
        fields = VideoSerializer.Meta.fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'video_file': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class VideoDeleteForm(forms.Form):
    pk = forms.IntegerField()