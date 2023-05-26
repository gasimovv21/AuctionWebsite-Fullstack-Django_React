from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class User(models.Model):
    name = models.CharField(
        verbose_name="User name",
        max_length=settings.USER_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(2)],
    )
    email = models.EmailField(
        verbose_name="User email",
        max_length=settings.USER_EMAIL_MAX_LENGTH,
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


# Done by Recep Enes Karatekin