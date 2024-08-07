from rest_framework.serializers import ModelSerializer

# Models
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser']
        
        
        