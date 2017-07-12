from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """Custom user model."""

    date_of_birth = models.DateField(null=True, blank=True)
