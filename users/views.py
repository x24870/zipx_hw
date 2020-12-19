from django.shortcuts import render, redirect
from django.urls import reverse
# from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import requests

def home(request):
    return render(request, 'users/home.html', {})

def get_data(request):
    url = "https://jsonplaceholder.typicode.com/users"
    json_data = requests.get(url).json()
    for data in json_data:
        username = data['name']
        email = data['email']
        catchPhrase = data['company']['catchPhrase']
        # print(username, email, catchPhrase)
        User = get_user_model()
        new_user = User.objects.create_user(
            username=username,
            email=email,
            catchPhrase=catchPhrase,
            password='',
        )
        
    return redirect(reverse('users:home'))
    
