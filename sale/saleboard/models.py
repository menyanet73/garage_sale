from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class UserProfile(models.Model):
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


class Item(models.Model):
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

    class Meta:
        ordering = ['-created']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title[:20]


class Photos(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(
        'Фото товара',
        upload_to='sale/',
        blank=True
    )

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = verbose_name
