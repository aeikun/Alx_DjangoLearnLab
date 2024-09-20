from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer

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
