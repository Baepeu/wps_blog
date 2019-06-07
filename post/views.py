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

class PostUpdate(UpdateView):
    model = Post
    template_name = 'post/post_update.html'
    fields = ['title','text','tag']
    # success_url => get_abslute_url

from django.urls import reverse_lazy

class PostDelete(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:post_list')

from django.utils.text import slugify

class PostCreate(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    fields = ['title', 'text', 'tag']

    def form_valid(self, form):
        # 작성자 매칭 - form.instance.author_id = self.request.user.id
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)
        return super().form_valid(form)

from tagging.views import TaggedObjectList

class PostTaggedObjectList(TaggedObjectList):
    model = Post
    allow_empty = True
    template_name = 'post/post_list.html'









