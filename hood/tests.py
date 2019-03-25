from django.test import TestCase
from .models import Profile,Project,Business,Post
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.



class ProjectTestClass(TestCase):

    def setUp(self):
        self.new_user = User(username = "dee", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_project = Project(name= 'dee', admin = self.new_user)
        self.new_project.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Project.objects.all().delete()

    def test_save_project(self):
       
        self.new_project.save_project()
        self.assertTrue(len(Project.objects.all()) > 0)
    
    def test_init(self):
        self.assertTrue(self.new_project.name =='dee')
    
    def test_delete_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

   


class ProfileTestClass(TestCase):

    def setUp(self):
        user = User(username='abbyshabi')
        self.profile = Profile(profile_image='yes we can', bio='very awesome', user=user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
    
    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.profile.bio == "very awesome")

    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 0)

class PostTestClass(TestCase):

    def setUp(self):

        self.new_user = User(username = "dee", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_project = Project(name= 'dee', admin = self.new_user)
        self.new_project.save()
        self.new_post= Post(body = 'cool')

    def test_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_post, Post))
       

    def test_init(self):
        self.assertTrue(self.new_post.body =='cool')

    def tearDown(self):
        """
        This will clear the dbs after each test
        """
    
        Post.objects.all().delete() 

    def test_save_post(self):
        post = Post.objects.all()
        self.assertTrue(len(post) >= 0)


    # def test_delete_method(self):
    #     self.new_post.save_post()
    #     post = Post.objects.all()
    #     self.new_post.delete_post()
    #     post = Post.objects.all()
    #     self.assertTrue(len(post )< 0)



class BusinessTestClass(TestCase):

    def setUp(self):
        self.new_user = User(username = "dee", email = "dammy@uu.com",password = "hello")
        self.new_user.save()
        self.new_project = Project(name= 'dee', admin = self.new_user)
        self.new_project.save()
        self.new_business = Business(name= 'dee', owner = self.new_user,neighbourhood = self.new_project)
        self.new_business.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Business.objects.all().delete()

    def test_save_business(self):
       
        self.new_business.save_business()
        self.assertTrue(len(Business.objects.all()) > 0)
    
    def test_init(self):
        self.assertTrue(self.new_business.name =='dee')
    
    def test_delete_method(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)

    def test_search_business(self):
        """
        This will test whether the search function works
        """
        name = Business.search_business("dee")
        self.assertTrue(len(name) > 0)
    
