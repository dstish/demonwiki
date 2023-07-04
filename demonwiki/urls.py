from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demon_souls.urls')),
    path('tinymce/', include('tinymce.urls'))

]