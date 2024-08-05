from rest_framework import serializers
from ..models.deck_model import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'name', 'user', 'deck_leader', 'tcg', 'deck_type', 'colors', 'photo', 'wins', 'losses', 'created_at', 'updated_at']
