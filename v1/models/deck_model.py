from django.db import models
from ..models.card_model import Card
from ..models.user_model import User
from ..enums.deck_type_enum import DeckType
from ..enums.tcg_type_enum import TcgType
from ..enums.color_enum import MtgColor

class Deck(models.Model):
    name = models.CharField(max_length=150, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    deck_leader = models.OneToOneField(Card, on_delete=models.SET_NULL, null=True, blank=True)

    tcg = models.CharField(max_length=50, null=False, choices=TcgType.choices())
    deck_type = models.CharField(max_length=50, null=True, choices=DeckType.choices())
    # colors and photo need to set to null when the leader is deleted. Create logic for this functionality.
    colors = models.CharField(max_length=255, blank=True, null=True)
    photo = models.URLField(null=True, blank=True)
    # wins and losses will need to be adjusted later to reflect the total wins and total losses across all pods and games played with this deck.
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.deck_leader:
            self.photo = self.deck_leader.img
            self.colors = self.deck_leader.colors
        super().save(*args, **kwargs)

