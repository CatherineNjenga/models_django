from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    """A new post in our blog."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = get_user_model()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    """Return a string representation of the model."""
    return self.text




