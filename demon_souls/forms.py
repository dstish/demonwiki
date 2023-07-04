from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .item_models import Item
from tinymce.widgets import TinyMCE

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Item.CATEGORIES)
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'category']
