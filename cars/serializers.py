from rest_framework import serializers
from .models import Car
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_picture(self, obj):
        # Возвращаем относительный URL, чтобы Vite проксировал /media к Django
        if obj.picture:
            return obj.picture.url
        return None

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
