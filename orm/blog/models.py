from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Post(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    opened_at = models.DateTimeField()


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
