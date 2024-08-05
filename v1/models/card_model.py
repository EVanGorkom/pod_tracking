from django.db import models
from ..models.color_model import Color
from ..models.deck_model import Deck

class Card(models.Model):
    name = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color, through='CardColor')
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    mana_cost = models.CharField(max_length=50)
    cmc = models.IntegerField(default=0)
    type_line = models.CharField(max_length=255)
    # set = models.CharField(max_length=255)
    rarity = models.CharField(max_length=50)
    cmdr_legal = models.CharField(max_length=50)
    img = models.URLField()
    purchase_uris = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name