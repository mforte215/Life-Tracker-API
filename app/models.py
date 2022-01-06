from django.db import models
from django.conf import settings
import uuid
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class TrackerItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    action_date_time = models.DateTimeField(editable=True)
    tags = models.ManyToManyField(Tag, related_name="Items")