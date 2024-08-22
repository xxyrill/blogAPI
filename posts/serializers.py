from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

# this converts the Post model to and from JSON
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

# this converts the User model to and from JSON
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)

# serializers converts data from a complex type (like Django model instance)
# into a simple, standard format like JSON which can be easily sent over the web.

# if this code is converted into django model, it looks like this:

# from django.db import models
# class Post(models.Model):
# id = models.UUIDField()
# author = models.Charfield(max_length=100)
# title = models.Charfield(max_length=100)