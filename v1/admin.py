from django.contrib import admin
from .models.user_model import User
from .models.deck_model import Deck
from .models.card_model import Card
from .models.card_color_model import CardColor
from .models.color_model import Color

admin.site.register(User)
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(CardColor)
admin.site.register(Color)

