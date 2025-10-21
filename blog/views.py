from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save(update_fields=['views'])
        return response

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'image',]
    success_url = reverse_lazy("blog:post_list")

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content', 'image',]
    
    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.pk])

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("blog:post_list")
