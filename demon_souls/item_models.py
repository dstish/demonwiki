from django.contrib.auth import get_user_model
from django.db import models
import os


def get_image_upload_path(instance, filename):
    category = instance.category
    upload_path = os.path.join('items/images', category, filename)
    return upload_path


class Item(models.Model):
    CATEGORIES = [
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('ring', 'Ring'),
        ('magic', 'Magic'),
        ('character', 'Character'),
        ('boss', 'Boss'),
        ('location', 'Location'),
    ]

    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    image = models.ImageField(upload_to=get_image_upload_path)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
