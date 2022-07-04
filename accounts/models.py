from django.contrib.auth.models import AbstractUser
from django.db import models, IntegrityError


class CustomUser(AbstractUser):
    following = models.ManyToManyField("CustomUser", blank=True)

    def __str__(self) -> str:
        return f"{self.username}"

    def is_following(self, user, currently_following) -> bool:
        """
        A method to verify if the current user is already following the target user.

        Args:
            user (CustomUser): Target user object from the database
            currently_following (List: pk): List of the currently followed targets of the user.

        Returns:
            bool: True if it's being followed. False if not.

        """

        if user in currently_following:
            return True
        else:
            return False

    def follow_user(self, username):
        """
        This method adds the target user to the current user following list.

        Args:
            username (str): The target username which the current user wants to follow.

        Returns:
            tuple: A success value, if added True, if not False. An object, if True the target user,
            if False an exception.

        """

        user_to_follow = CustomUser.objects.get(username=username)
        if user_to_follow is None:
            return False, IntegrityError
        else:
            self.following.add(user_to_follow.id)
            self.save()
            return True, user_to_follow

    def unfollow_user(self, username):
        """
        This method removes the target user from the current user following list.
        Args:
            username (str): The target username which the current user wants to follow.

        Returns:
            tuple: A success value, if added True, if not False. An object, if True the target user,
            if False an exception.

        """

        user_to_unfollow = CustomUser.objects.get(username=username)

        if user_to_unfollow is None:
            return False, IntegrityError
        else:
            self.following.remove(user_to_unfollow.id)
            self.save()
            return True, user_to_unfollow
