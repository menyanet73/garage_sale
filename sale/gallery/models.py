from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from core.utils.transileration import transliteration_rus_eng
from saleboard.models import Item


class Photo(models.Model):
    """Фото"""
    image = models.ImageField('Фото', upload_to='gallery/')

    def __str__(self) -> str:
        return transliteration_rus_eng(self.image) + "_" + str(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Gallery(models.Model):
    photos = models.ManyToManyField(
        Photo,
        verbose_name='Фотографии',
        blank=True
    )
    item = models.OneToOneField(
        'saleboard.Item',
        on_delete=models.CASCADE,
        verbose_name='Объявление',
        related_name='gallery',
    )

    def __str__(self) -> str:
        return transliteration_rus_eng(self.photos)+'_'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


"""Создание галереи при создании объявления"""

@receiver(post_save, sender=Item)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля при регистрации пользователя"""
    if created:
        Gallery.objects.create(item=instance)

