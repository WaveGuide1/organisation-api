from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user model
    """

    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'email', 'phone']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'password', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user with a hashed password and return the user
        """
        user = User(
            email=validated_data['email'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            phone=validated_data.get('phone', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
