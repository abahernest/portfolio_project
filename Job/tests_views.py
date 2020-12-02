from django.test import TestCase,Client
from datetime import date
from Job.models import *

class HomeViewTestCase (TestCase):
    def setUp (self):
        self.now=date.today()
        self.client = Client()
        Project.objects.create(image="../media/image/20180305_130006.jpg",title="projectA",technologies="1,2,3,4,5",description="descrA",link="https://test-linkA.com",date=self.now)
        Project.objects.create(image="../media/image/20180305_130006.jpg",title="projectB",technologies="1,2,3,4,5",description="descrB",link="https://test-linkB.com",date=self.now)

    def test_get_response (self):
        #Test url responses
        print ("Method: test_get_response")
        res = self.client.get('')
        
        #checks that response is 200 OK.
        self.assertEqual (res.status_code,200)

        #checks that rendered context contains 2 projects
        self.assertEqual (len(res.context['projects']),2)