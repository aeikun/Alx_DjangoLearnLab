from rest_framework import generics, viewsets, permissions
from .models import Post, Comment
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Like
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    # Use get_object_or_404 to retrieve the post
    post = get_object_or_404(Post, pk=pk)
    
    # Use get_or_create to like the post or prevent multiple likes
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
    # Use get_object_or_404 to retrieve the post
    post = get_object_or_404(Post, pk=pk)

    # Check if the like exists and delete it
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    notification_data = [
        {
            "actor": notification.actor.username,
            "verb": notification.verb,
            "target": str(notification.target),
            "timestamp": notification.timestamp,
            "read": notification.read
        } for notification in notifications
    ]
    return Response(notification_data, status=status.HTTP_200_OK)

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Get the users the current user is following
        following_users = user.following.all()
        # Return posts authored by the following users, ordered by creation date (most recent first)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
