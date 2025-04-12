from django.contrib import admin
from django.db.models import Avg

from review_service_api.settings import LIST_PER_PAGE
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('name',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('name',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category',
        'get_genre',
        'count_reviews',
        'get_rating'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('name',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('name', 'year', 'category')

    def get_genre(self, object):
        return '\n'.join((genre.name for genre in object.genre.all()))

    get_genre.short_description = 'Жанр/и твору'

    def count_reviews(self, object):
        return object.reviews.count()

    count_reviews.short_description = 'Кількість відгуків'

    def get_rating(self, object):
        rating = object.reviews.aggregate(average_score=Avg('score'))
        return round(rating.get('average_score'), 1)

    get_rating.short_description = 'Рейтинг'


@admin.register(GenreTitle)
class GenreTitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'genre',
        'title'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('genre',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('title',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'score',
        'pub_date',
        'title'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('author', 'score', 'pub_date')
    list_per_page = LIST_PER_PAGE
    search_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'pub_date',
        'review'
    )
    empty_value_display = 'значення відсутнє'
    list_filter = ('author', 'pub_date')
    list_per_page = LIST_PER_PAGE
    search_fields = ('author',)


admin.site.site_title = 'Адміністрування review_service_api'
admin.site.site_header = 'Адміністрування review_service_api'
