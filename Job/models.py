from django.db import models
from datetime import date

# Create your models here.
class Job(models.Model):
    image= models.ImageField (upload_to="image/",blank=True)
    job_title=models.CharField (max_length=300)
    company=models.CharField(max_length=300)
    start_date=models.DateField()
    end_date= models.DateField(null=True)
    achievement1=models.TextField()
    achievement2=models.TextField()
    achievement3=models.TextField()

    def __str__ (self):
        return self.job_title


class Project(models.Model):
    image= models.ImageField (upload_to="image/",blank=True)
    title=models.CharField (max_length=300)
    technologies=models.CharField (max_length=300)
    description=models.TextField ()
    link=models.URLField()
    date=models.DateField()
    
    def __str__ (self):
        return self.title

class Volunteer (models.Model):
    image= models.ImageField (upload_to="image/",blank=True)
    organization=models.CharField(max_length=300)
    position= models.CharField(max_length=300)
    achievement1=models.TextField()
    achievement2=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField(null=True)

    def __str__ (self):
        return self.organization

class Certificates (models.Model):
    image= models.ImageField (upload_to="image/",blank=True)
    organization=models.CharField(max_length=300)
    name=models.CharField(max_length=500)
    description=models.TextField()
    link=models.URLField()
    date_received=models.DateField()
        
    def __str__ (self):
        return self.name
    
class Resume (models.Model):
    resume=models.FileField()