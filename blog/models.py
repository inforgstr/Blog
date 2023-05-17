from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_created=True)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    image = models.ImageField(upload_to="Posts/%Y/%m/%d/", null=True, blank=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title
