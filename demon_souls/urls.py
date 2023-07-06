from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create_item'),
    path('category/weapon/', views.category_view_factory('weapon'),
         name='weapon_category'),
    path('category/armor/', views.category_view_factory('armor'),
         name='armor_category'),
    path('category/ring/', views.category_view_factory('ring'), name='ring_category'),
    path('category/magic/', views.category_view_factory('magic'),
         name='magic_category'),
    path('category/character/', views.category_view_factory('character'),
         name='character_category'),
    path('category/boss/', views.category_view_factory('boss'), name='boss_category'),
    path('category/location/', views.category_view_factory('location'),
         name='location_category'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('add_comment/<int:item_id>/', views.add_comment, name='add_comment')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
