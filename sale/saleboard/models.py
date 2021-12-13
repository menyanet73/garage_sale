from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel, TreeForeignKey


User = get_user_model()


class UserProfile(models.Model):
    """Отклонения от встроенной модели пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='phone',
    )
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
    )

    class Meta:
        verbose_name = 'Данные профиля'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.user.username


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
    gallery = models.ForeignKey(
        'gallery.Gallery',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    slug = models.SlugField("url", max_length=50)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title[:20]
