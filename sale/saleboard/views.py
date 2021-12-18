from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render


from .models import Images, Item
from users.models import UserProfile
from .forms import ItemForm, ImagesForm


def index(request):
    post_list = (
        Item.objects
        .select_related('category')
    )
    first_image_list = []
    #Снова костыль
    for item in post_list:
        first_image_list.append(Images.objects.filter(item=item).first)
    print(first_image_list)
    paginator = Paginator(post_list, settings.PAGE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'saleboard/index.html'
    context = {
        'title': 'Главная страница',
        'page_obj': page_obj,
        'first_image_list': first_image_list,
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
        instance=item,
    )


    if form.is_valid():
        itemobj = Item.objects.create(
            author=request.user,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            price=form.cleaned_data['price'],
            category=form.cleaned_data['category'],
        )
        for f in request.FILES.getlist('images'):
            photo = Images.objects.create(item=itemobj, images=f)
            #photo.images.save(f.name, f)
            #photo.save()
        return redirect('saleboard:index')
        
        
    print(form.errors)
    context ={
        'title': 'Создать объявление',
        'form': form
    }
    return render(request, 'saleboard/item_create.html', context)

@login_required
def item_delete(request, slug):
    item = get_object_or_404(Item, slug=slug)
    if item.author == request.user:
        item.delete()
        return redirect('saleboard:index')