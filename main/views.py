from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def about(requests):
    return render(requests, 'about.html')

def resume(requests):
    return render(requests, "resume.html")

def contact(requests):
    return render(requests, "contact.html")