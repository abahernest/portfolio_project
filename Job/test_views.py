from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from Job.models import *

class HomeViewTestCase (TestCase):
    @classmethod
    def setUpTestData (cls):
        now=date.today()
        NUMBER_OF_OBJECTS =5
        for count in range(NUMBER_OF_OBJECTS):
            Project.objects.create(image="../media/image/albert.jpg",title="projectA",technologies="1,2,3,4,5",description="descrA",link="https://test-linkA.com",date=now)
            Job.objects.create(image="../media/image/albert.jpg",job_title=f"title{count+1}",company=f"company{count+1}",start_date=now,end_date=now,achievement1=f"achievement{count+1}")
            Certificates.objects.create(image="../media/image/albert.jpg",organization=f"organization{count+1}",name=f"certificate{count+1}",description=f"description{count+1}",link=f"https://link{count+1}.com",date_received=now)
            Volunteer.objects.create(image="../media/image/albert.jpg",organization=f"company{count+1}",position=f"role{count+1}",start_date=now,end_date=now)
            Skill.objects.create(title=f"title{count+1}",description=f"descr {count+1}")
        Resume.objects.create(resume="../media/image/albert.jpg")
        Resume.objects.create(resume="../media/image/bitgrit.png")

    def test_Homeview_url_exists_at_desired_endpoints (self):
        #Test url responses
        res = self.client.get('')
        #checks that response is 200 OK.
        self.assertEqual (res.status_code,200)

    def test_total_number_of_project_object_is_5 (self):
        res=self.client.get('')
        self.assertEqual (len(res.context['projects']), 5)

    def test_total_number_of_job_object_is_5 (self):
        res=self.client.get('')
        self.assertEqual (len(res.context['jobs']), 5)

    def test_total_number_of_volunteer_object_is_5 (self):
        res=self.client.get('')
        self.assertEqual (len(res.context['volunteers']), 5)

    def test_total_number_of_certificates_object_is_5 (self):
        res=self.client.get('')
        self.assertEqual (len(res.context['certificates']), 5)

    def test_total_number_of_skills_object_is_5 (self):
        res=self.client.get('')
        self.assertEqual (len(res.context['skills']), 5)

    def test_resume_object_is_last_uploaded (self):
        res=self.client.get('')
        resume=Resume.objects.order_by("-id")
        self.assertEqual (res.context['resume'], resume[0])

    def test_Homeview_url_accessible_by_name (self):
        res=self.client.get(reverse('home'))
        self.assertEqual (res.status_code,200)

    def test_HomeView_uses_correct_template (self):
        res=self.client.get(reverse('home'))
        self.assertEqual (res.status_code,200)
        self.assertTemplateUsed (res, 'jobs/home.html')
