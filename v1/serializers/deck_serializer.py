from rest_framework import serializers
from ..models.deck_model import Deck
from ..enums.color_enum import MtgColor

class DeckSerializer(serializers.ModelSerializer):
    colors = serializers.ChoiceField(choices=MtgColor.choices())

    class Meta:
        model = Deck
        fields = ['id', 'name', 'user', 'deck_leader', 'tcg', 'deck_type', 'colors', 'photo', 'wins', 'losses', 'created_at', 'updated_at']
