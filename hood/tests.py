from django.test import TestCase
from .models import NeighbourHood, Profile, Business

# Create your tests here.
class UserTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.testuser = User(username="user", email="test@mail.com")

    def test_instance(self):
        self.assertIsInstance(self.testuser, User)

    def test_save_user(self):
        self.assertFalse(self.testuser in User.objects.all())
        self.testuser.save()
        self.assertTrue(self.testuser in User.objects.all())
        self.testuser.delete()

    def test_delete_user(self):
        self.testuser.save()
        self.assertTrue(self.testuser in User.objects.all())
        self.testuser.delete()
        self.assertFalse(self.testuser in User.objects.all())

class BusinessTestClass(TestCase):

    #Set Up method
    def setUp(self):
        self.laflare = Business(business_name = 'Cali', business_email = 'cali@gmail.com', user = 'laflare', neighbourHood = 'Kilimani')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare,Business))


class ProfileTestClass(TestCase):

    #Set Up method
    def setUp(self):
        self.laflare = Profile(username = 'laflare', email = 'laflare@gmail.com', user = 'laflare', neighbourHood = 'Kilimani')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare,Profile))


class NeighbourhoodTestClass(TestCase):

    #Set Up method
    def setUp(self):
        self.laflare = Neighbourhood(neighbourhood_name = 'Alpha', neighbourhood_location = 'Kilimani', occupants = '2', user = 'laflare')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.laflare,NeighbourHood))


    def tearDown(self):
    Business.objects.all().delete()
    Profile.objects.all().delete()
    NeighbourHood.objects.all().delete()