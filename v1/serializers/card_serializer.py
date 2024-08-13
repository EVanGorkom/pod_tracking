from rest_framework import serializers
from ..models.card_model import Card
from ..enums.color_enum import MtgColor

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "name", "cmc", "mana_cost", "colors", "type_line", "rarity", "cmdr_legal", "img", "purchase_uris", "created_at", "updated_at"]