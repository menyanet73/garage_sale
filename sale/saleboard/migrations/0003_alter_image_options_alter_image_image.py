# Generated by Django 4.0 on 2021-12-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleboard', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Изображение'),
        ),
    ]