from rest_framework import serializers
from ..models.color_model import Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']
