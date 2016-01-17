from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100) #Validates
    last_name = models.CharField(max_length=100) #validates
    bio = models.TextField()
    email = models.EmailField(unique=True) #validates
    profile_image = models.FilePathField() # make default image
    human_image = models.FilePathField() # make human photo
    best_image = models.FilePathField() # make it the best photo
    interest_image = models.FilePathField()
    location = models.CharField(max_length=60) #the location
    industry = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    active = models.BooleanField() # determine if account is active or not
    reports = models.IntegerField() # a number of reported profile problems, if its above 5 account automatically shuts down
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name



class Dating(models.Model):
    user_profile = models.OneToOneField(User)
    smoking = models.CharField(max_length=30)
    height = models.CharField(max_length=20)
    body_type = models.CharField(max_length=40)
    ethnicity = models.CharField(max_length=30)
    sexual_orientation = models.CharField(max_length=20)
    future_plans = models.TextField(max_length=200)
    education = models.CharField(max_length=20)
    income = models.CharField(max_length=30)
    religion = models.CharField(max_length=20)

class Hobby(models.Model):
    hobby_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

class HobbyPerson(models.Model):
    hobby_id = models.ForeignKey(Hobby)
    user_id =  models.ForeignKey(User)

class Message(models.Model):
    user_to = models.ForeignKey(User, related_name="user_to") # who the message is too
    user_from = models.ForeignKey(User, related_name="user_from") # the user id the message is from
    bulk_message = models.TextField() #validates
    date = models.DateTimeField() # validates
    title_message = models.CharField(max_length=20)

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account    
