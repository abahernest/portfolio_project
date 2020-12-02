from django.test import TestCase,Client
from Job.models import *
from datetime import date
import unittest

class ProjectModelTestCase (TestCase):
    def setUp (self):
        self.now=date.today()
        self.NUMBER_OF_OBJECTS=2 
        for count in range(self.NUMBER_OF_OBJECTS):
            Project.objects.create(title=f"project{count}",technologies="1,2,3,4,5",description=f"descr{count}",link=f"https://test-link{count}.com",date=self.now)
        

    def test_image_field_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('image').verbose_name
        self.assertEqual(field_name,"image")
    
    def test_title_field_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('title').verbose_name
        self.assertEqual(field_name,"title")

    def test_technologies_field_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('technologies').verbose_name
        self.assertEqual(field_name,"technologies")

    def test_description_field_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('description').verbose_name
        self.assertEqual(field_name,"description")

    def test_link_field_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('link').verbose_name
        self.assertEqual(field_name,"link")

    def test_date_ield_labels (self):
        project=Project.objects.get(id=1)
        field_name = project._meta.get_field('date').verbose_name
        self.assertEqual(field_name,"date")

    def test_object_name_is_title (self):
        #Tests if the object name is equal to the title of the project
        project=Project.objects.get(id=1)
        self.assertEqual (project.title,str(project))

    def test_total_number_of_objects (self):
        #Test if the total number of project objects created is NUMBER_OF_OBJECTS
        projects=Project.objects.values()
        self.assertEqual (len(projects),self.NUMBER_OF_OBJECTS)


class JobModelTestCase (TestCase):
    def setUp (self):
        self.now=date.today()
        self.NUMBER_OF_OBJECTS=2 
        for count in range(self.NUMBER_OF_OBJECTS):
            Job.objects.create(job_title=f"title{count+1}",company=f"company{count+1}",start_date=self.now,end_date=self.now,achievement1=f"achievement{count+1}")

    def test_image_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('image').verbose_name
        self.assertEqual(field_name,"image")
    
    def test_job_title_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('job_title').verbose_name
        self.assertEqual(field_name,"job title")

    def test_company_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('company').verbose_name
        self.assertEqual(field_name,"company")

    def test_start_date_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('start_date').verbose_name
        self.assertEqual(field_name,"start date")

    def test_end_date_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('end_date').verbose_name
        self.assertEqual(field_name,"end date")

    def test_achievement1_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('achievement1').verbose_name
        self.assertEqual(field_name,"achievement1")
    
    def test_achievement2_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('achievement2').verbose_name
        self.assertEqual(field_name,"achievement2")

    def test_achievement3_field_labels (self):
        job=Job.objects.get(id=1)
        field_name = job._meta.get_field('achievement3').verbose_name
        self.assertEqual(field_name,"achievement3")
    
    def test_object_name_is_job_title_and_company (self):
        #Tests if the object name is equal to the title of the project
        job=Job.objects.get(id=1)
        self.assertEqual (f"{job.job_title} at {job.company}",str(job))

    def test_total_number_of_objects (self):
        #Test if the total number of project objects created is NUMBER_OF_OBJECT
        job=Job.objects.values()
        self.assertEqual (len(job),self.NUMBER_OF_OBJECTS)




class CertificatesModelTestCase (TestCase):
    def setUp (self):
        self.now=date.today()
        self.NUMBER_OF_OBJECTS=2 
        for count in range(self.NUMBER_OF_OBJECTS):
            Certificates.objects.create(organization=f"organization{count+1}",name=f"certificate{count+1}",description=f"description{count+1}",link=f"https://link{count+1}.com",date_received=self.now)

    def test_image_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('image').verbose_name
        self.assertEqual(field_name,"image")
    
    def test_organization_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('organization').verbose_name
        self.assertEqual(field_name,"organization")

    def test_certificate_name_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('name').verbose_name
        self.assertEqual(field_name,"name")

    def test_date_received_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('date_received').verbose_name
        self.assertEqual(field_name,"date received")

    def test_description_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('description').verbose_name
        self.assertEqual(field_name,"description")

    def test_link_field_labels (self):
        cert=Certificates.objects.get(id=1)
        field_name = cert._meta.get_field('link').verbose_name
        self.assertEqual(field_name,"link")
    
    def test_object_name_is_organization_and_certificate_name (self):
        #Tests if the object name is equal to the title of the project
        cert=Certificates.objects.get(id=1)
        self.assertEqual (f"{cert.organization},{cert.name}" , str(cert))

    def test_total_number_of_objects (self):
        #Test if the total number of project objects created is NUMBER_OF_OBJECT
        cert=Certificates.objects.values()
        self.assertEqual (len(cert),self.NUMBER_OF_OBJECTS)

