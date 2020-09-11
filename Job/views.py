from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from decouple import config

# Create your views here.

def home (request):
    jobs=Job.objects.order_by("-end_date")
    projects=Project.objects.order_by("-date")
    volunteer=Volunteer.objects.order_by("-end_date")
    certificate=Certificates.objects.order_by("-date_received")
    resume=Resume.objects.order_by('-id')[0]
    success_message=''
    if request.method =="POST":
        contact(request)
        success_message="Thanks!! I've Received Your Message"

        return render(request, 'jobs/home.html', {'jobs':jobs,'projects':projects,'volunteer':volunteer,'certificates':certificate,'success_message':success_message,'resume':resume})

    return render(request, 'jobs/home.html', {'jobs':jobs,'projects':projects,'volunteer':volunteer,'certificates':certificate,'resume':resume})
def contact (request):
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        mail_subject = "New Message from {}".format(sender_name)
        message = request.POST['message']
        # send_message(request,sender_name,sender_email,mail_subject,message)
        send_mail(mail_subject, message, sender_email, ['abahernesto@gmail.com'])
