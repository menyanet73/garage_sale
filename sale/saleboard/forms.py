from django import forms

from .models import Item, Images


class ItemForm(forms.ModelForm):
    images = forms.ImageField(
        label=u'Добавить фото',
        widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'category', )

class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ('images', )