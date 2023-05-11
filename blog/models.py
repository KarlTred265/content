from django.db import models
import uuid
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = CloudinaryField('image', null=True, blank=True)
    body = models.TextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title