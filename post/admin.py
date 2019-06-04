from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','created','updated']
    ordering = ['-updated','-created']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

