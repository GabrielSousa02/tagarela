from django.db import models

from accounts.models import CustomUser


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=280, blank=False)
    author = models.ForeignKey(CustomUser, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}.\n by {self.author} - {self.created}"

    class Meta:
        ordering = ["-created"]
