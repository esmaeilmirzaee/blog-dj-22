from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    like_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('allauth.urls')),
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<str:slug>/edit', PostUpdateView.as_view(), name='edit'),
    path('<str:slug>/delete', PostDeleteView.as_view(), name='delete'),
    path('<str:slug>/detail', PostDetailView.as_view(), name='detail'),
    path('like/<str:slug>/detail', like_view, name='like')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
