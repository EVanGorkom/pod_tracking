from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from ..models.card_model import Card
from ..models.user_model import User
from ..enums.deck_type_enum import DeckType

class Deck(models.Model):
    name = models.CharField(max_length=150, required=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck_leader = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, required=False)

    tcg = models.CharField(max_length=50, required=True)
    deck_type = models.CharField(max_length=50, required=True, choices=DeckType.choices())
    colors = models.CharField(max_length=100, default='', blank=True)
    photo = models.URLField(null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

@receiver(post_save, sender=Deck)
def update_deck_fields(sender, instance, **kwargs):
    if instance.deck_leader:
        instance.photo = instance.deck_leader.img
        instance.colors = ', '.join([color.name for color in instance.deck_leader.colors.all()])
        instance.save()

@receiver(pre_delete, sender=Deck)
def delete_leader_card(sender, instance, **kwargs):
    if instance.deck_leader:
        instance.deck_leader.delete()

