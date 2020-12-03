from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from decouple import config

# Create your views here.

def home (request):
    jobs=Job.objects.order_by("-end_date")
    projects=Project.objects.order_by("-date")
    volunteers=Volunteer.objects.order_by("-end_date")
    certificate=Certificates.objects.order_by("-date_received")
    resume=Resume.objects.order_by('-id')
    skills = Skill.objects.all()
    context={'jobs':jobs,'projects':projects,'volunteers':volunteers,'certificates':certificate,'skills':skills}
    
    #fetch url to the most recently uploaded resume 
    if len(resume)>0:
        context.update({'resume':resume[0]})
    
    #if post request, call contactViews function
    if request.method =="POST":
        contact(request)
        success_message="Thanks!! I've Received Your Message"
        context.update({'success_message':success_message})

        return render(request, 'jobs/home.html',context )
    
    return render(request, 'jobs/home.html',context )


def contact (request):
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        mail_subject = f"New Message from {sender_name}"
        message = f"Sender Email: {sender_email}\nMessage: {request.POST['message']}"
      
        send_mail(mail_subject, message, sender_email, ['abahernesto@gmail.com'])
