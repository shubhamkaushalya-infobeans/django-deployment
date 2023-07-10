from django.db import models
from django.contrib.auth.models import User as MainUser

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email =  models.TextField(max_length=50,unique=True)
    # Returns the last entry
    def __str__(self):
        return self.first_name

class Books(models.Model):
    book_id = models.IntegerField(primary_key=True,unique=True)
    book_name = models.TextField(max_length=50)

    def __str__(self):
        return self.book_name

class StudentBooks(models.Model):
    rel_id      = models.IntegerField(primary_key=True)
    book_id     = models.ForeignKey(Books, on_delete=models.CASCADE,)
    student_id  = models.ForeignKey(Student, on_delete=models.CASCADE,)

class User(models.Model):
    firstname   = models.CharField(max_length=200)
    lastname    = models.CharField(max_length=200)
    email       = models.CharField(max_length=200)

class UserProfileMoreInformationForm(models.Model):

    # relation of this form with existing signup page
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE,)

    # Additional info
    web_url = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='first_app/profile_pics',blank=True)

