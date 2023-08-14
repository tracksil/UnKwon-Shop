from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, db_index=True, error_messages={"unique": _("User with this email already exist.")}
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.BigIntegerField(
        unique=True, error_messages={"unique": _("User with this email already exist.")}
    )
    birthday = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
