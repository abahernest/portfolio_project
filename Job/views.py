from django.shortcuts import render
from .models import *
from django.core.mail import send_mail,EmailMessage

# Create your views here.

def home (request):
    jobs=Job.objects.order_by("-end_date")
    projects=Project.objects.order_by("-date")
    volunteer=Volunteer.objects.order_by("-end_date")
    certificate=Certificates.objects.order_by("-date_received")
    success_message=''
    if 'email' in request.GET:
        sender_name = request.GET['name']
        sender_email = request.GET['email']
        mail_subject = request.GET['subject']
        message = "{} has sent you a new message via your Portfolio Website:\n\n{}".format(sender_name, request.GET['message'])
        print("SUCCESSFULLY SENT")
        print("SUCCESSFULLY SENT")
        send_mail(mail_subject, message, sender_email, ['abahernesto@gmail.com'])
        success_message="Your message has been sent. Thank you!"

    return render(request, 'jobs/home.html', {'jobs':jobs,'projects':projects,'volunteer':volunteer,'certificates':certificate,'success_message':success_message})
