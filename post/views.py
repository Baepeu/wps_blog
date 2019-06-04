from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'post/index.html')

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

from .models import *

class PostList(ListView):
    model = Post
    paginate_by = 1
    template_name = 'post/post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'category_slug' in self.kwargs:
            try:
                category = Category.objects.get(slug=self.kwargs['category_slug'])
                queryset = queryset.filter(category=category)
            except:
                pass

        return queryset

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'








