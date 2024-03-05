from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category2(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    body = models.TextField()
    image = models.FileField(upload_to='post_images')
    first_category = models.ForeignKey(Category1, on_delete=models.CASCADE)
    second_category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' - ' + self.name
