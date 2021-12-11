# Generated by Django 4.0 on 2021-12-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name': 'фото', 'verbose_name_plural': 'фото'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Данные профиля', 'verbose_name_plural': 'Данные профиля'},
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Укажите стоимость товара', max_digits=8, verbose_name='стоимость товара'),
        ),
    ]
