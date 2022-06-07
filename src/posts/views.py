from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, PostView, Comment, Like
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post_obj = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post_obj
            comment.save()
            return redirect('detail', slug=post_obj.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        post_detail_obj = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=post_detail_obj)
        return post_detail_obj


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


def like_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs:
        # delete like
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
