from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
