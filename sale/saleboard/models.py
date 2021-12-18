from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from core.utils.transileration import transliteration_rus_eng
from users.models import User


class Category(MPTTModel):
    """Категория"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_inserion_by = ['name']
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    """Объявление"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='название товара',
        help_text='Введите название товара',
    )
    description = models.TextField(
        verbose_name='описание товара',
        help_text='Введите описание товара'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='стоимость товара',
        help_text='Укажите стоимость товара',
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items',
    )
    slug = models.SlugField("url", max_length=50, unique=True)


    def get_image_filename(instance, filename):
        title = instance.item.title
        slug = transliteration_rus_eng(title)
        return "post_images/%s-%s" % (slug, filename)

    def __str__(self):
        return self.title[:20]

    def mod_save(self, *args, **kwargs):
        """Метод-костыль, для правильного сохранения slug"""
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = transliteration_rus_eng(self.title) + "_" + str(self.pk)
        self.mod_save()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class Images(models.Model):
    item = models.ForeignKey(
        Item,
        default=None,
        on_delete=models.CASCADE,
        related_name='images',
    )
    images = models.ImageField(
        upload_to='gallery/%d-%s/',
        verbose_name='Изображение',
    )

    def __str__(self) -> str:
        return self.item.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'