from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Models
from .models import Election, ElectoralProfile, MediaOutlet

# Serializers
from .serializers import ElectionSerializer, ElectoralProfileSerializer, MediaOutlet

# JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Views
class ElectionViewSet(ViewSet): # Election 
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        
        queryset = Election.objects.all()
        
        elections = ElectionSerializer(queryset, many=True)
        
        return Response(elections.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        
        queryset = get_object_or_404(Election, id=pk)
        
        election = ElectionSerializer(instance=queryset)
        
        return Response(election.data, status=status.HTTP_200_OK)

class ElectoralProfileViewSet(ViewSet): # Electoral Profile 
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        
        queryset = ElectoralProfile.objects.all()

        electoralProfile = ElectoralProfileSerializer(queryset, many=True)

        return Response(electoralProfile.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        
        queryset = get_object_or_404(ElectoralProfile, id=pk)
        
        election = ElectoralProfileSerializer(instance=queryset)
        
        return Response(election.data, status=status.HTTP_200_OK)