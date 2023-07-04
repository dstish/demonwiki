from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .item_models import Item

@receiver(pre_save, sender=Item)
def set_item_author(sender, instance, **kwargs):
    if not instance.author:
        user = get_user_model().objects.first()
        instance.author = user
