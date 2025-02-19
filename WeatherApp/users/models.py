from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [('manager', 'Manager'), ('user', 'User')]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    city = models.ForeignKey('weather.City', on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

