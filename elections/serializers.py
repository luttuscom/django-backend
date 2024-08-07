from rest_framework.serializers import ModelSerializer

# Models
from .models import Election, ElectoralProfile, MediaOutlet

class ElectionSerializer(ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'


class ElectoralProfileSerializer(ModelSerializer):
    class Meta:
        model = ElectoralProfile
        fields = '__all__'

class MediaOutletSerializer(ModelSerializer):
    class Meta:
        model = MediaOutlet
        fields = '__all__'
