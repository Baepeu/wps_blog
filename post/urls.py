from django.urls import path, re_path
from .views import *

app_name = 'post'

urlpatterns = [
    path('tags/<tag>/', PostTaggedObjectList.as_view(), name='post_taggedlist'),
    path('tags/', TagList.as_view(), name='tag_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('detail/<slug>/', PostDetail.as_view(), name='post_detail'),
    path('<category_slug>/', PostList.as_view(), name='post_list_with_category'),
    path('', PostList.as_view(), name='post_list')
]