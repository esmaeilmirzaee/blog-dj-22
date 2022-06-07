from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, PostView, Comment, Like
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    class_form = PostForm
    model = Post
    success_url = '/'
    fields = [
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Creating',
        })
        return context


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'slug'
    )


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
