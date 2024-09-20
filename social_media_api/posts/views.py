from rest_framework import generics, viewsets, permissions
from .models import Post, Comment, Like
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    # Ensure that permissions.IsAuthenticated is checked
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Use generics.get_object_or_404 explicitly
    post = generics.get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target_content_type=ContentType.objects.get_for_model(post),
        target_object_id=post.id
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    # Ensure that permissions.IsAuthenticated is checked
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Use generics.get_object_or_404 explicitly
    post = generics.get_object_or_404(Post, pk=pk)

    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
