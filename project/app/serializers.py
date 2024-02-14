from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'owner']
    
class TaskCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status']