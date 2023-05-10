from django.db import models
from django.conf import settings

class User(models.Model):
    name = models.CharField(
        verbose_name="User name",
        max_length=settings.USER_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name="User email",
        max_length=settings.USER_EMAIL_MAX_LENGTH,
        unique=True,
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        verbose_name="User age",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
