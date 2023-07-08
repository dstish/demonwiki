from django.contrib.auth.admin import UserAdmin
from .user_models.models import CustomUser
from django.contrib import admin
from .article_models.item_models import Comment, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


admin.site.register(Item, ItemAdmin)

# Определяем новый класс администратора для модели CustomUser


class CustomUserAdmin(UserAdmin):
    # Определяем отображаемые поля модели в административной панели
    list_display = ('username', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


# Регистрируем модель CustomUser и класс администратора в административной панели
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment)
