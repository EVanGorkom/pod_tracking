from django.contrib import admin
from .models.user_model import User
from .models.deck_model import Deck
from .models.card_model import Card

admin.site.register(User)
admin.site.register(Deck)
admin.site.register(Card)
