from django.contrib import admin

from review_service_api.settings import LIST_PER_PAGE

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role'
        # 'confirmation_code'
    )
    empty_value_display = 'значення відсутнє'
    list_editable = ('role',)
    list_filter = ('username',)
    list_per_page = LIST_PER_PAGE
    search_fields = ('username', 'role')
