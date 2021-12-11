from django.contrib import admin

from .models import Item, UserProfile, Photos


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'description',
        'price',
        'created'
    )
    search_fields = ('title', 'description',)
    list_filter = ('created',)
    empty_valut_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(UserProfile)
admin.site.register(Photos)
