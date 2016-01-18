from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


# class AccountManager(BaseUserManager):
#     def create_user(self, email, password=None, **kwargs):
#         if not email:
#             raise ValueError('Users must have a valid email address.')
#
#         if not kwargs.get('first_name'):
#             raise ValueError('Users must have a valid First Name.')
#
#         account = self.model(
#             email=self.normalize_email(email), first_name=kwargs.get('first_name')
#         )
#
#         account.set_password(password)
#         account.save()
#
#         return account
#
#     def create_superuser(self, email, password, **kwargs):
#         account = self.create_user(email, password, **kwargs)
#
#         account.is_admin = True
#         account.save()
#
#         return account



class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100) #Validates
    last_name = models.CharField(max_length=100) #validates
    bio = models.TextField()
    tagline = models.CharField(max_length=140, blank=True)
    email = models.EmailField(unique=True) #validates
    profile_image = models.FilePathField() # make default image
    human_image = models.FilePathField() # make human photo
    best_image = models.FilePathField() # make it the best photo
    interest_image = models.FilePathField()
    location = models.CharField(max_length=60) #the location
    industry = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    active = models.BooleanField(default="false") # determine if account is active or not
    reports = models.IntegerField(default="0") # a number of reported profile problems, if its above 5 account automatically shuts down
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = AccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin





class Dating(models.Model):
    user_profile = models.OneToOneField(Account)
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
    user_id =  models.ForeignKey(Account)

class Message(models.Model):
    user_to = models.ForeignKey(Account, related_name="user_to") # who the message is too
    user_from = models.ForeignKey(Account, related_name="user_from") # the user id the message is from
    bulk_message = models.TextField() #validates
    date = models.DateTimeField() # validates
    title_message = models.CharField(max_length=20)
