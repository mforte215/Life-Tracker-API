from django.contrib import admin
from .models import Tag, TrackerItem

# Register your models here.
admin.site.register(Tag)
admin.site.register(TrackerItem)
