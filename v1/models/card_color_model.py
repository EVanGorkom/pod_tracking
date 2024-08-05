from django.db import models
from ..models.card_model import Card
from ..models.color_model import Color

class CardColor(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("card", "color")

    def __str__(self) -> str:
        return f"{self.card.name} - {self.color.name}"