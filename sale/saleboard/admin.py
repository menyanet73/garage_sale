from django.contrib import admin

from .models import Category, Images, Item
from gallery.models import Photo, Gallery


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'category',
        'title',
        'description',
        'price',
        'created',
        'slug',

    )
    search_fields = ('title', 'description',)
    list_filter = ('created',)
    empty_valut_display = '-пусто-'
    prepopulated_fields = {'slug': ('author', 'title')}


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Images)
