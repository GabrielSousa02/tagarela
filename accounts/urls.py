# accounts/urls.py
from django.urls import path
from knox import views as knox_views

from .views import (
    login_user,
    signup_user,
    detail_user,
    list_users,
    follow_user,
    unfollow_user,
)


urlpatterns = [
    path("", list_users),
    path("detail", detail_user),
    path("follow", follow_user),
    path("unfollow", unfollow_user),
    path("signup", signup_user),
    path("login", login_user),
    path("logout", knox_views.LogoutView.as_view()),
    path("logoutall", knox_views.LogoutAllView.as_view()),
]
