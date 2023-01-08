from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views, viewsets
from rest_framework.response import Response
from django.shortcuts import redirect
from .serializers import UserSerializer
from django.contrib.auth.models import Group,User 

 
class RegisterAPIView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(views.APIView):
    def post(self, request):
        # Authenticate the user
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user
            login(request, user)
            user = User.objects.get(username=username)
            if user.groups.filter(name='Creators').exists():
                return redirect('creatorView')
            #Return a success response
            else:
            #return Response(status=status.HTTP_200_OK) 
                return redirect('homeView')
        else:
            # Return an error message
            return redirect('loginView')

 