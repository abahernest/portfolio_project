from django.shortcuts import render
from .models import Job

# Create your views here.

def home (requests):
    jobs=Job.objects.order_by("-end_date")
    return render(requests, 'jobs/home.html', {'jobs':jobs})
