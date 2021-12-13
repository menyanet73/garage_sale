from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render


from .models import Item


def index(request):
    post_list = (
        Item.objects
        .select_related('gallery', 'category')
        .prefetch_related('gallery__photos')
        # .values(
        #     'title', 'description', 'price',
        #     'gallery__photos', 'category__name'
        # )
    )
    paginator = Paginator(post_list, settings.PAGE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'saleboard/index.html'
    context = {
        'title': 'Главная страница',
        'page_obj': page_obj,
    }
    return render(request, template, context)
