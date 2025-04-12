from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)
from django.db import models

from review_service_api.settings import LENGTH_TEXT

User = get_user_model()


class Category(models.Model):

    name = models.CharField(
        max_length=256,
        verbose_name='Назва',
        db_index=True
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='slug',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Слаг категорії містить неприпустимий символ'
        )]
    )

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ('name',)

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Genre(models.Model):

    name = models.CharField(
        max_length=75,
        verbose_name='Hазва',
        db_index=True
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='slug',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Слаг категорії містить неприпустимий символ'
        )]
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'
        ordering = ('name',)

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class Title(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Hазва',
        db_index=True
    )
    year = models.PositiveIntegerField(
        verbose_name='рік випуску',
        validators=[
            MinValueValidator(
                0,
                message='Значення року не може бути негативним'
            ),
            MaxValueValidator(
                int(datetime.now().year),
                message='Значення року не може бути більшим за поточний'
            )
        ],
        db_index=True
    )
    description = models.TextField(
        verbose_name='опис',
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
        verbose_name='жанр'

    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='категорія',
        null=True
    )

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        ordering = ('-year', 'name')

    def __str__(self):
        return self.name[:LENGTH_TEXT]


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='фільм'
    )

    class Meta:
        verbose_name = 'Відповідність жанру та фільму'
        verbose_name_plural = 'Таблиця відповідності жанрів та фільмів'
        ordering = ('id',)

    def __str__(self):
        return f'{self.title} належить жанру/ам {self.genre}'


class Review(models.Model):
    text = models.TextField(
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Aвтор'
    )
    score = models.PositiveIntegerField(
        verbose_name='Oцінка',
        validators=[
            MinValueValidator(
                1,
                message='Введена оцінка нище допустимої'
            ),
            MaxValueValidator(
                10,
                message='Введена оцінка вище допустимої'
            ),
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публікації',
        db_index=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='фільм',
        null=True
    )

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            ),
        )

    def __str__(self):
        return self.text[:LENGTH_TEXT]


class Comment(models.Model):
    text = models.TextField(
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Aвтор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публікациї',
        db_index=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='відгук',
    )

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:LENGTH_TEXT]
