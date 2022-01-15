
from asyncore import write
from rest_framework import serializers
from .models import Post,Comment

class AllPostsSerializer(serializers.ModelSerializer):
    
    comments = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='body',
     )
    likes = serializers.IntegerField(
    source='likes.count', 
    read_only=True
    )
    class Meta:
        model = Post
        fields = ['id','title','description','created_at','comments','likes']



class CommentSerializer(serializers.ModelSerializer):
    body = serializers.CharField(write_only = True)
    class Meta:
        model = Comment
        fields = ['id', 'body']
        
class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'description','created_at']
    

