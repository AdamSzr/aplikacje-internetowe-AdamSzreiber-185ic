from rest_framework import serializers
from .models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta: # specyfy what fields should be visible for api user.
        model= User
        fields= ('id','name','surname')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author','title','body','created_at','updated_at')

    