from django.shortcuts import render
from .models import Blog


# Create your views here.
def home (requests):
    blogs=Blog.objects
    return render(requests,"blogs/home.html",{'blogs':blogs})
