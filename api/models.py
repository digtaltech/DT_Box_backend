from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Data(models.Model):
    username = models.ForeignKey('auth.User', related_name='data', on_delete=models.CASCADE) # Юзер которому принадлежит тур FK
    # place = models.ForeignKey(Place, related_name='places', on_delete=models.CASCADE)
    sessionId = models.TextField(max_length=200) # Название text
    data = models.TextField(max_length=500) # Описание text

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
