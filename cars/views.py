from django.shortcuts import render
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.views.generic import TemplateView
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Создаем JWT токены для нового пользователя
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    
class FrontendAppView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        if not password:
            return Response({'error': 'Password cannot be empty'}, status=400)
        if ' ' in password:
            return Response({'error': 'Password cannot contain spaces'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        }, status=201)

@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response({'username': request.user.username})
    return Response({'error': 'Not authenticated'}, status=401)
    
def vue_app(request):
    return render(request, 'index.html')
