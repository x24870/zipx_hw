from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model

import requests

User = get_user_model()

def home(request):
    show_print_user_btn = True if User.objects.all() else False
    context = {
        'show_print_user_btn': show_print_user_btn
    }
    return render(request, 'users/home.html', context=context)

def get_data(request):
    if request.method == 'POST':
        url = "https://jsonplaceholder.typicode.com/users"
        json_data = requests.get(url).json()
        for data in json_data:
            username = data['name']
            email = data['email']
            catchPhrase = data['company']['catchPhrase']
            print(username, email, catchPhrase)
            User = get_user_model()
            new_user = User.objects.create_user(
                username=username,
                email=email,
                catchPhrase=catchPhrase,
                password='',
            )

    return redirect(reverse('users:home'))
    
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        catchPhrase = request.POST['catchphrase']
        print(username, email, catchPhrase)
        new_user = User.objects.create_user(
            username=username,
            email=email,
            catchPhrase=catchPhrase,
            password='',
        )

    return redirect(reverse('users:home'))

def print_users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users/print_users.html', context=context)