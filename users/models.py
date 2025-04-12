from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from review_service_api.settings import LENGTH_TEXT

from .enums import UserRoles


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name="Ім'я користувача",
        unique=True,
        db_index=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message="'Ім'я користувача містить неприпустимий символ'"
        )]
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="ім'я",
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="прівище",
        blank=True
    )
    bio = models.TextField(
        verbose_name='біографія',
        blank=True
    )
    role = models.CharField(
        max_length=20,
        verbose_name='роль',
        choices=UserRoles.choices(),
        default=UserRoles.user.name
    )

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ('id',)

    def __str__(self):
        return self.username[:LENGTH_TEXT]

    @property
    def is_admin(self):
        return self.role == UserRoles.admin.name

    @property
    def is_moderator(self):
        return self.role == UserRoles.moderator.name

    @property
    def is_user(self):
        return self.role == UserRoles.user.name
