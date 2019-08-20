from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(object):
    """Manage User Profile"""

    def create_user(self,email,name,password=None):
        """Create a new user Profile"""
        if not email:            #email is mendatory in this so check email is empty or null
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user = user.set_password(password)
        user.save(using=self._db)  #support multiple databases in future.

        return user

    def create_superuser(self,email,name,password):
        """Create a new super user of system"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive Full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive Short name"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.email
