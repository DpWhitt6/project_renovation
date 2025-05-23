from django.db import models
from django.contrib.auth.models import User # Import models to connect

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)