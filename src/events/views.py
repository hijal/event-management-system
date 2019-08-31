from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect



def home_page(request):
    return render(request, 'home_page.html', {})


def about_page(request):
    return render(request, 'about.html', {})

def gallery_page(request):
    return render(request, 'gallery.html', {})

def contact_page(request):
    return render(request, 'contact.html', {})