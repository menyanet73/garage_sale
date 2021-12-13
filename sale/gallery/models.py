from django.db import models


class Photo(models.Model):
    """Фото"""
    image = models.ImageField('Фото', upload_to='gallery/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Gallery(models.Model):
    photos = models.ManyToManyField(Photo, verbose_name='Фотографии')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
