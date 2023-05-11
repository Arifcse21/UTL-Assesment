from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from uuid import uuid4
# Create your models here.


class UserModelCustomManager(BaseUserManager):
    def all_superuser(self):
        """
            Custom model manager for retrieving all superuser
        """
        try:
            superusers = self.model().objects.filter(is_staff=True, is_superuser=True)

            return superusers

        except self.model.DoesNotExist:
            return None


class User(AbstractBaseUser):
    uuid = models.CharField(max_length=32, default=uuid4())

    objects = UserModelCustomManager

