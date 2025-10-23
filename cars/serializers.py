from rest_framework import serializers
from .models import Car

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
