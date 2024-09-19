from rest_framework import serializers
#from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ['username', 'password', 'bio', 'profile_picture']  # Add necessary fields

    def create(self, validated_data):
        # Create the user using create_user to handle password hashing
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        token = Token.objects.create(user=user)
        
        return user
