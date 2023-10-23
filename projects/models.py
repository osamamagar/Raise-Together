from django.db import models
# from django.contrib.auth.models import User
from accounts.models import MyUser
from django.utils import timezone
from categories.models import Category





class Project(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(max_length=300)
    total_target = models.DecimalField(max_digits=10, decimal_places=2, default=250000)
    start_time = models.DateTimeField(auto_now_add=False,default=timezone.now)
    end_time = models.DateTimeField(auto_now=False,default=None)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)
    current_target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='projects')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tag',null=True)


    def __str__(self):
        return self.name

class Multi_Picture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        return f'/media/{self.image}'


class Rating(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.title}: {self.rating}"
