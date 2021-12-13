from django.contrib import admin

from .models import Category, Item, UserProfile
from gallery.models import Photo, Gallery

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'category',
        'title',
        'description',
        'price',
        'created',

    )
    search_fields = ('title', 'description',)
    list_filter = ('created',)
    empty_valut_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Gallery)
