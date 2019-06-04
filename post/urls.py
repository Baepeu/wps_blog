from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', PostList.as_view(), name='post_list')
]