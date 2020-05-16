from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.urls import base, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
# Create your views here.

from .models import Post


class PostListView(ListView):
    paginate_by = 3
    queryset = Post.objects.filter(status='p').order_by('-created_at')


class PostDetailView(DetailView):
    queryset = Post.objects.filter(status='p').order_by('-created_at')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    success_url = reverse_lazy('post_list')
    template_name_suffix = '_update_form'
