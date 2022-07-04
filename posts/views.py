from rest_framework import generics, permissions
from knox.auth import TokenAuthentication

from posts.models import Post
from posts.serializers import PostSerializer


class GeneralFeedListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user

        # Selecting posts from users other than the current user
        posts = Post.objects.exclude(author_id=current_user.id)[0:10]

        return posts


class PostListCreateView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user

        # Create a list of users that are being followed by the current user
        currently_following = [user.id for user in current_user.following.all()]

        # Filter posts based on the list of followed users
        posts = Post.objects.filter(author__in=currently_following)[0:10]

        return posts

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
