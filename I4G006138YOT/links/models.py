from django.db import models
from django.contrib.auth import get_user_model
from .utils import generate_random_id

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    descriptions = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    # Custom save method
    def save(self, *args, **kwargs):
        self.identifier = generate_random_id()
        super(Link, self).save(*args, **kwargs)
