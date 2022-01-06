from django.contrib.auth.models import User, Group
from .models import TrackerItem, Tag
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

class TrackerItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackerItem
        fields = ['id', 'name', 'createdAt', 'createdBy', 'description', 'action_date_time', 'tags']