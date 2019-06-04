from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from tagging.fields import TagField
from django.shortcuts import resolve_url
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('post:post_list_with_category', self.slug)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    text = RichTextUploadingField()
    material = models.FileField(upload_to='material/%Y/%m/%d',blank=True)
    tag = TagField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " at " + self.created.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return resolve_url('post:post_detail', self.slug)