from django.contrib.auth import get_user_model
from django.db import models


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

    item_id = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items/images/')
    category = models.CharField(max_length=100, choices=CATEGORIES, default='weapon')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
