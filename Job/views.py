from django.shortcuts import render
from .models import Job

# Create your views here.

def home (requests):
    jobs=Job.objects
    return render(requests, 'jobs/home.html', {'jobs':jobs})
