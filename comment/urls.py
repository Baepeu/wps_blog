from django.urls import path
from .views import *
urlpatterns = [
    path('add_comment/', add_comment, name='add_comment'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
]