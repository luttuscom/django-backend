from django.contrib.auth.models import User
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Tokens
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class UsersViewSet(viewsets.ViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):

        queryset = User.objects.all()
        
        user = UserSerializer(instance=queryset, many=True)
        
        return Response(user.data)
    

class RegisterViewSet(viewsets.ViewSet):
    
    def create(self, request):
        
        request.data['is_staff'] = False
        request.data['is_active'] = True
        request.data['is_superuser'] = False
        
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'detail': 'Invalid object'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
            
        user = User.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
            
        serializer = UserSerializer(instance=user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


class LoginViewSet(viewsets.ViewSet):
    
    def create(self, request):
        
        try:
            userObject = get_object_or_404(User, email=request.data['email'])    
        except KeyError:
            userObject = get_object_or_404(User, username=request.data['username'])    
    
        user = UserSerializer(instance=userObject)


        if not userObject.check_password(request.data['password']):
        
            return Response({
                'detail': 'Incorrect password'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Creating Token
        refresh = RefreshToken.for_user(userObject)

        return Response({
            'user_data': user.data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        }, status=status.HTTP_200_OK)
        
        
