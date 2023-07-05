from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth import get_user_model
# from .item_models import Item
import os

User = get_user_model()


def get_image_upload_path(instance, filename):
    category = instance.category
    upload_path = os.path.join('items/images', category, filename)
    return upload_path


class CustomUserManager(UserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self.create_user(username, password, **extra_fields)


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


# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=100, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'username'

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin


class Comment(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.item.name}'
