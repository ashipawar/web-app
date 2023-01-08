from django.shortcuts import render,HttpResponse,redirect
import requests 
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group,User 
from videodistribution.forms import VideoForm,VideoDeleteForm
from rest_framework.test import APIClient


def test_func(user):
    # Return True if the user is not authenticated, False otherwise
    return not user.is_authenticated

def test_creator(user):
    # Return True if the user is not authenticated, False otherwise
    return user.groups.filter(name='Creators').exists()

# Create your views here. 
@login_required(login_url='/login')
def homeView(request): 
    response = requests.get("http://127.0.0.1:8000/api/videos/")

    if response.status_code == 200:
        data = response.json()
    # Do something with the data
    else:
     # Handle the error 
        pass  
    context = {'data': data } 

    return render(request,'Site/home.html',context)

@user_passes_test(test_func)
def registerView(request): 
    form = UserRegistrationForm()
    if request.method == 'POST':
        # Send a POST request to the RegisterAPIView API view
        response = requests.post('http://localhost:8000/auth-api/register/', data=request.POST)
        if response.status_code == 201:
            # Registration was successful
            return redirect('loginView')
        else: 
            return redirect('registerView')
    else:
        # Render the registration form
        return render(request, 'Site/register.html',{'form':form})

@user_passes_test(test_func)
def loginView(request):
    form = UserLoginForm()
    if request.method == 'POST':
        # Validate the form
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Get the user's login credentials
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Send a POST request to the LoginAPIView API view
            response = requests.post('http://localhost:8000/auth-api/login/',
             data={'username': username, 'password': password})
            if response.status_code == 200:
                # Login was successful as user 
               user = User.objects.get(username=username)
               if user.groups.filter(name='creators').exists():
                    return redirect('Creator/dashboard.html')
               else:
                    return redirect('home_view')
            else:
                # Login failed, return an error message
                return HttpResponse('Please try again!')
    else:
        # Render the login form
        return render(request, 'Site/login.html', {'form': form})



def logoutView(request):
    # Log out the user
    logout(request)
    # Redirect the user to the login page
    return redirect('loginView')



def watchView(request,id):  
    response = requests.get(f'http://127.0.0.1:8000/api/videos/{id}') 
    movie = response.json()
    return render(request,'Site/watch.html',{'movie':movie})


@user_passes_test(test_creator)
def creatorView(request):

    return render(request, 'Creator/dashboard.html')


@user_passes_test(test_creator)
def createView(request):
    # Get the data for the new video from the request 
    form = VideoForm(request.POST, request.FILES)
    if form.is_valid():
        # Create a DRF APIClient
        api_client = APIClient()
        # Send a POST request to the API to create the new video
        response = api_client.post('http://127.0.0.1:8000/api/videos/', data = { 
            'title':form.cleaned_data['title'], 
            'description':form.cleaned_data['description'], 
            'video_file':form.cleaned_data['video_file'], 
            'thumbnail':form.cleaned_data['thumbnail'], 
            'category':form.cleaned_data['category']
        }, format='multipart')
        
        # Check the response status code
        if response.status_code == 201:
            # If the request was successful, get the serialized data for the new video
            return redirect('creatorView')
        else:
            # If the request was not successful, return an error response
            return HttpResponse('Error creating video', status=response.status_code)
    else:
        form = VideoForm()
    return render(request, 'Creator/create.html', {'form': form})
     
@user_passes_test(test_creator)
def deleteView(request):
     if request.method == 'POST':
        # Get the primary key of the video to be deleted from the form
        pk = request.POST['pk']
        # Create a DRF APIClient
        api_client = APIClient()
        # Send a DELETE request to the API to delete the video
        response = api_client.delete('http://127.0.0.1:8000/api/videos/{}/'.format(pk))
        
        # Check the response status code
        if response.status_code == 204:
            # If the request was successful, redirect to the video list page
            return redirect('creatorView')
        else:
            # If the request was not successful, return an error response
            return HttpResponse('Error deleting video', status=response.status_code)
     else:
        # Create an instance of the VideoDeleteForm form
        form = VideoDeleteForm()
        # Render the template 'Creator/delete.html' with the form
        return render(request, 'Creator/delete.html', {'form': form})