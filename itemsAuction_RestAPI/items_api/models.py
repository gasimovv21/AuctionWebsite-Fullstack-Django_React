import requests

from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MinValueValidator


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
        auto_now_add=False
    )
    updated_at = models.DateTimeField(
        auto_now=False
    )

    def __str__(self):
        return self.name


class ItemInAuction(models.Model):
    name = models.TextField(
        verbose_name="Item name",
        max_length=settings.ITEM_NAME_MAX_LENGHT,
        unique=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(1)],
        verbose_name="Price of item"
    )
    item_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Owner',
        help_text='Determine which user the item belongs to.',
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