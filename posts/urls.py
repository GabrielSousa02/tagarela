# posts/urls.py

from django.urls import path

from posts.views import PostListCreateView

urlpatterns = [
    path("post", PostListCreateView.as_view()),
]
