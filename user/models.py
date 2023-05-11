from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4
# Create your models here.


class UserModelCustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def all_active_user(self):
        """
            Custom model manager for retrieving all active user
        """
        try:
            active_users = self.model().objects.filter(is_active=True)

            return active_users

        except self.model.DoesNotExist:
            return None


def maintain_serial():
    last_id = User.objects.all().order_by('id').last()
    if last_id:
        return last_id.id + 1
    return 1


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(editable=False, unique=True, primary_key=True, default=maintain_serial)
    uuid = models.CharField(max_length=50, default=uuid4())
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserModelCustomManager()

    USERNAME_FIELD = 'email'




