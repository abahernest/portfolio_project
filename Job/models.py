from django.db import models

# Create your models here.
class Job(models.Model):
    image= models.ImageField (upload_to="image/")
    job_title=models.CharField (max_length=300)
    company=models.CharField(max_length=300)
    start_date=models.DateField()
    end_date= models.DateField()
    summary=models.TextField()
