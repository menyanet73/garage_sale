from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from core.utils.transileration import transliteration_rus_eng

User = get_user_model()


class UserProfile(models.Model):
    """Отклонения от встроенной модели пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profiles',
    )
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
    )
    email = models.EmailField(verbose_name='Электронная почта')
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars/',
        blank=True,
        null=True,
    )
    created = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True,
    )
    slug = models.CharField(max_length=70, unique=True)
    #TODO Нужна функция, подтверждающая профиль с номером телефона
    confirmed = models.BooleanField(
        verbose_name='Подтверждение',
        default=False,
    )

    def get_full_name(self):
        return self.first_name+' '+self.last_name

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = transliteration_rus_eng(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили'


""" Возможно пригодится.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    #Создание профиля при регистрации пользователя
    if created:
        UserProfile.objects.create(user=instance)
"""
