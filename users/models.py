from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    bio = models.TextField(max_length=500, blank=True, verbose_name='О себе')
    location = models.CharField(max_length=100, blank=True, verbose_name='Местоположение')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    reputation = models.IntegerField(default=0, verbose_name='Репутация')
    is_online = models.BooleanField(default=False, verbose_name='Онлайн')
    last_seen = models.DateTimeField(auto_now=True, verbose_name='Последний визит')
    ip_address = models.CharField(max_length=45, blank=True, null=True, verbose_name='IP-адрес регистрации')
    is_banned = models.BooleanField(default=False, verbose_name='Забанен')
    ban_reason = models.TextField(max_length=500, blank=True, null=True, verbose_name='Причина бана')
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __str__(self):
        return f'Профиль {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
