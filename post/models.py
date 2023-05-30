from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = HTMLField(max_length=10000, null=False, blank=False)
    image = models.ImageField(upload_to="posters/%Y-%m", null=True, blank=True)
    like_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=400, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content}:{self.is_active}"
