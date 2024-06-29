from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    pass
    def get_absolute_url(self):
        return f'/'
    