
from django.contrib import admin
from django.urls import path
from django.contrib.admin import site

urlpatterns = [
    path(r'admin/', site.urls),
]
