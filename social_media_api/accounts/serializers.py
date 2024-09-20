from rest_framework import serializers
#from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'followers_count', 'following_count']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

# Custom User Serializer for registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    # Manually specify password as CharField
    password = serializers.CharField(write_only=True)  # This explicitly uses serializers.CharField()

    class Meta:
        model = get_user_model()  # Use custom user model
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Manually create the user without automatic methods
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Handle password manually
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )

        # Manually create a token for the new user
        Token.objects.create(user=user)

        return user