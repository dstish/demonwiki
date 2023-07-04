from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .item_models import Item
from django.shortcuts import render, redirect
from .forms import ItemForm


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'home.html')

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('item_detail', item_id=item.item_id)
    else:
        form = ItemForm()

    return render(request, 'item_create.html', {'form': form})

def item_detail(request, item_id):
    item = Item.objects.get(item_id=item_id)
    author_username = item.author.username if item.author else None
    return render(request, 'item_detail.html', {'item': item, 'author_username': author_username})


def category_view_factory(category):
    def category_view(request):
        items = Item.objects.filter(category=category)
        return render(request, 'category.html', {'items': items, 'category': category})

    return category_view
