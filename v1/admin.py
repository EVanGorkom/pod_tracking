from django.contrib import admin
from .models.card_model import Card
from .models.color_model import Color
from .models.card_color_model import CardColor

admin.site.register(Card)
admin.site.register(Color)
admin.site.register(CardColor)

# Register your models here.
