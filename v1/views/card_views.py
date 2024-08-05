from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from ..services.card_service import CardService
from ..serializers import CardSerializer
from ..models.card_model import Card
from ..models.color_model import Color

COLORS = {
    "W": "White",
    "U": "Blue",
    "B": "Black",
    "R": "Red",
    "G": "Green",
    "C": "Colorless"
}

# todo: build this service as a POST which expects a specific card name from the FE. FE should utilize the
  # auto-complete route to find and preview cards before clicking a 'save' button which sends the POST request to the backend with the name of the card to search for/save.

@api_view(["POST"])
def create_card(request):
  query = request.GET.get('query')
  if query:
    card_data = CardService.search_cards(query)
    for data in card_data:
      card = Card.objects.create(
        name=data.get('name'),
        mana_cost=data.get('mana_cost'),
        cmc=data.get('cmc'),
        type_line=data.get('type_line'),
        rarity=data.get('rarity'),
        cmdr_legal=data.get('legalities').get('commander'),
        img=data.get('image_uris').get('normal'),
        purchase_uris=data.get('purchase_uris').get('tcgplayer'),
        created_at=datetime.now(),
        updated_at=datetime.now()
      )

      if len(data.get('colors_identity')) == 0:
          colors = ["C"]
      colors = data.get('colors_identity', [])

      for color_abbreviation in colors:
          color = Color.objects.filter(name=COLORS[color_abbreviation]).first()
          if color:
              card.colors.add(color)
      card.save()

    serializer = CardSerializer(card)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)