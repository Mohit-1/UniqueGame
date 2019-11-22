from django.contrib import admin
from django.urls import path
from base.views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', base_view)
]
