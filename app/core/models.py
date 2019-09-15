from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                         PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):


    def create_user(self, email, password=None, **extra_fields):
        """Creates New User and SAVE() """
        if not email:
            raise ValueError('users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):


        """Custom user model that supports using emails instead of username"""
        email = models.EmailField(max_length=254, unique=True)
        name = models.CharField(max_length=50)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects = UserManager()

        USERNAME_FIELD = 'email'
