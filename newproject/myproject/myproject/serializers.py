from rest_framework import serializers
from .models import *
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

        
