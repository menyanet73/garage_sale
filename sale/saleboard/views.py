from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render


from .models import Images, Item
from users.models import UserProfile
from .forms import ItemForm, ImagesForm


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
        instance=item,
    )


    if form.is_valid():
        
        # if form.cleaned_data['images']:
            # for imgobj in form.images:
            #     image = Images(item=item)
            #     images_form = ImagesForm(
            #         request.POST,
            #         files=imgobj,
            #         instance=image
            #     )
            #     if images_form.is_valid():
            #         form.save()
            #         images_form.save()
            #         return redirect('saleboard:index')

            #     else:
            #         print(images_form.errors)
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


    # item = Item(author=request.user)
    # form = ItemForm(
    #     request.POST or None,
    #     files=request.FILES or None,
    #     instance=item
    # )
    # #gallery_form = 
    # if form.is_valid():
    #     form.save()
    #     #TODO Заменить редирект
    #     return redirect('saleboard:index')
    # context = {
    #     'title': 'Новое объявление',
    #     'form': form,
    # }
    # return render(request, 'saleboard/item_create.html', context)
