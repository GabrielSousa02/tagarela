# posts/urls.py

from django.urls import path

from posts.views import PostListCreateView
from posts.views import GeneralFeedListView

urlpatterns = [
    path("post", PostListCreateView.as_view()),
    path("post/general", GeneralFeedListView.as_view()),
]
