from django.urls import path, re_path
from .views import *

app_name = 'post'

urlpatterns = [
    path('<slug:category_slug>/', PostList.as_view(), name='post_list_with_category'),
    path('', PostList.as_view(), name='post_list')
]