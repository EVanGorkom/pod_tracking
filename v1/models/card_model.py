from django.db import models
from ..enums.color_enum import MtgColor

class Card(models.Model):
    name = models.CharField(max_length=255)

    cmc = models.IntegerField(default=0)
    mana_cost = models.CharField(max_length=50)
    colors = models.CharField(max_length=255, blank=True, null=True)
    type_line = models.CharField(max_length=255)
    rarity = models.CharField(max_length=50)
    cmdr_legal = models.CharField(max_length=50)
    img = models.URLField()
    purchase_uris = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
