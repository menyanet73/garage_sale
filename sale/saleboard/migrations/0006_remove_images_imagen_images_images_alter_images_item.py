# Generated by Django 4.0 on 2021-12-17 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleboard', '0005_alter_images_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='imagen',
        ),
        migrations.AddField(
            model_name='images',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='images',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='saleboard.item'),
        ),
    ]
