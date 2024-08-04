from rest_framework import serializers
from ..models.card_model import Card
from .color_serializer import ColorSerializer

class CardSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ['name', 'mana_cost', 'cmc', 'type_line', 'rarity', 'cmdr_legal', 'img', 'purchase_uris', 'colors']