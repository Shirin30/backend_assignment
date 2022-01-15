from cgitb import lookup
from os import stat
from rest_framework.views import APIView
from authentication.models import User
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status,permissions,generics
from social.models import Post,Comment
from social.permissions import IsOwner

from social.serializers import CommentSerializer, PostSerializer,AllPostsSerializer

class AllPostsAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

# Create your views here.
class UserProfileAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request, format=None):
        cur_user = self.request.user
        profile_data = {
            'username': cur_user.username,
            'follower_count': cur_user.followers.count(),
            'following_count': cur_user.followers.count(),
        }
        return Response(profile_data,status.HTTP_200_OK)

class FollowAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, pk, format=None):
        cur_user = self.request.user
        try:
            follower = User.objects.get(id=pk)
        except:
            return Response({"User not found"},status.HTTP_404_NOT_FOUND)
        if cur_user in follower.followers.all():
            return Response({"You are already following this user"},status.HTTP_400_BAD_REQUEST)
        follower.followers.add(cur_user.id)
        cur_user.following.add(follower.id)
        return Response({"You successfully followed this user"},status.HTTP_200_OK)

class UnFollowAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, pk, format=None):
        cur_user = self.request.user
        try:
            follower = User.objects.get(id=pk)
        except:
            return Response({"User not found"},status.HTTP_404_NOT_FOUND)
        if cur_user not in follower.followers.all():
            return Response({"You are not a follower of this user"},status.HTTP_400_BAD_REQUEST)
        follower.followers.remove(cur_user.id)
        cur_user.following.remove(follower.id)
        return Response({"You successfully unfollowed this user"},status.HTTP_200_OK)

class PostsAPIView(generics.CreateAPIView):
    serializer_class=PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, serializer):
        serializer=PostSerializer(data = self.request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class CommentsAPIView(generics.CreateAPIView):
    serializer_class=CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk):
        serializer=CommentSerializer(data = self.request.data)
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response({"Post not found"},status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            comment = serializer.save(user=self.request.user)
            post.comments.add(comment)
            return Response(serializer.data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class PostSpeceficAPIView(generics.RetrieveDestroyAPIView):
    serializer_class=PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def get(self,request, pk, format=None):
        post = Post.objects.get(id = pk)
        data = {
            'id': post.id,
            'likes': post.likes.count(),
            'comments': post.comments.count(),
        }
        return Response(data,status.HTTP_200_OK)
class LikeAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, pk, format=None):
        cur_user = self.request.user
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response({"Post not found"},status.HTTP_404_NOT_FOUND)
        if cur_user in post.likes.all():
            return Response({"You have already liked this post"},status.HTTP_400_BAD_REQUEST)
        post.likes.add(cur_user.id)
        
        return Response({"You successfully liked this post"},status.HTTP_200_OK)

class UnLikeAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request, pk, format=None):
        cur_user = self.request.user
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response({"Post not found"},status.HTTP_404_NOT_FOUND)
        if cur_user not in post.likes.all():
            return Response({"You have not liked this post"},status.HTTP_400_BAD_REQUEST)
        post.likes.remove(cur_user.id)
        
        return Response({"You successfully unliked this post"},status.HTTP_200_OK)