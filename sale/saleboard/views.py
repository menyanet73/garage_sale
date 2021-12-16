from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render


from .models import Item
from users.models import UserProfile
from .forms import ItemForm


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


def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    author = UserProfile.objects.select_related('user').get(user=item.author)
    title = item.title[:30]
    template = 'saleboard/item_detail.html'
    context = {
        'title': title,
        'item': item,
        'author': author,
    }
    return render(request, template, context)


@login_required
def item_create(request):
    item = Item(author=request.user)
    form = ItemForm(
        request.POST or None,
        files=request.FILES or None,
        instance=item
    )
    #gallery_form = 
    if form.is_valid():
        form.save()
        #TODO Заменить редирект
        return redirect('saleboard:index')
    context = {
        'title': 'Новое объявление',
        'form': form,
    }
    return render(request, 'saleboard/item_create.html', context)
