from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)
    catchPhrase = models.CharField(max_length=1000, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email