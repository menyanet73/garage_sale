from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'phone',
        'email',
        'created',
    )
    search_fields = ('user', 'first_name', 'last_name',)
    list_filter = ('created',)
    empty_valut_display = '-пусто-'


admin.site.register(UserProfile, UserProfileAdmin)
