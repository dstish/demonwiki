from audioop import reverse
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

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Weapon(Item):
    ATTACK_TYPE = [
        ('standard', 'Standard'),
        ('special', 'Special'),
        ('magic', 'Magic'),
    ]

    damage = models.FloatField(null=True, blank=True)
    str = models.IntegerField(null=True, blank=True)
    dex = models.IntegerField(null=True, blank=True)
    attack_type = models.CharField(
        max_length=100, choices=ATTACK_TYPE, default='standard')


class Armor(Item):
    resist = models.IntegerField()


class Boss(Item):
    hp = models.IntegerField()


class Comment(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.item.name}'

    def delete_comment_url(self):
        return reverse('delete_comment', args=[self.id])
