from django.contrib import admin
from django.urls import path, include
from .views import get_tokens, show_tokens

urlpatterns = [
    path('', get_tokens, name='landing'),
    path('show/<int:pk>/', show_tokens, name='tokens'),
]