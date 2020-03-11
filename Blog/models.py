from django.db import models

# Create your models here.
class Blog (models.Model):
    image= models.ImageField (upload_to="image/")
    tag=models.CharField (max_length=300)
    presenter=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    full_information=models.TextField()
    date=models.DateField ()
