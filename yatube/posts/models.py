from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title
    

# Create your models here.
class Post(models.Model): 
    # Тип: TextField
    text = models.TextField() 
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        ) 
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE)
