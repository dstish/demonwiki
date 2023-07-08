from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .item_models import Item, Comment
from ckeditor.widgets import CKEditorWidget




class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class ItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Item.CATEGORIES)
    description = forms.CharField(widget=CKEditorWidget())
    damage = forms.FloatField(required=False)
    str = forms.IntegerField(required=False)
    dex = forms.IntegerField(required=False)
    attack_type = forms.ChoiceField(choices=Item.ATTACK_TYPE, required=False)

    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'category', 'damage', 'str', 'dex', 'attack_type']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
