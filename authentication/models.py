from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUser(AbstractUser):
    user_role = models.ForeignKey(
        UserRole,
        on_delete=models.CASCADE,
        related_name="User_role",
        null=True
    )
