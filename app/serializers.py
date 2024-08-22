from rest_framework import serializers
from .models import Royxat

class RoyxatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Royxat
        fields = '__all__'
