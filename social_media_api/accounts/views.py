from rest_framework import status, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        user = request.user

        if user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.following.add(user_to_follow)
        return Response({"message": "Successfully followed the user."}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        user = request.user

        if user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        user.following.remove(user_to_unfollow)
        return Response({"message": "Successfully unfollowed the user."}, status=status.HTTP_200_OK)

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        if request.user.is_following(user_to_follow):
            return Response({"detail": "Already following this user."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(user_to_follow)
        return Response({"detail": "User followed successfully."})

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if not request.user.is_following(user_to_unfollow):
            return Response({"detail": "Not following this user."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.unfollow(user_to_unfollow)
        return Response({"detail": "User unfollowed successfully."})
