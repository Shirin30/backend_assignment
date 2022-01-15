from django.urls import path
from .views import FollowAPIView, UnFollowAPIView,UserProfileAPIView,PostsAPIView,PostSpeceficAPIView,LikeAPIView,UnLikeAPIView,CommentsAPIView, AllPostsAPIView
from authentication.views import LoginAPIView


urlpatterns = [
    path('follow/<int:pk>', FollowAPIView.as_view(), name="follow"),
    path('unfollow/<int:pk>', UnFollowAPIView.as_view(), name="unfollow"),
    path('like/<int:pk>', LikeAPIView.as_view(), name="follow"),
    path('unlike/<int:pk>', UnLikeAPIView.as_view(), name="unfollow"),
    path('user', UserProfileAPIView.as_view(), name="user data"),
    path('posts/', PostsAPIView.as_view(), name="post"),
    path('posts/<int:pk>', PostSpeceficAPIView.as_view(), name="post detail"),
    path('comment/<int:pk>', CommentsAPIView.as_view(), name="comment detail"),
    path('allposts/', AllPostsAPIView.as_view(), name="all posts"),
    path('authenticate',LoginAPIView.as_view(),name='login')
   
    
]
