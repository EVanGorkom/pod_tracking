from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from v1.utils import process_colors
from ..serializers.card_serializer import CardSerializer
from ..enums.color_enum import MtgColor
from ..models.deck_model import Deck
from ..models.user_model import User
import pdb

# This will expect a JSON package of the data we care about from the FE after the user has already chosen the 'leader' they want from the data

# todo: Configure CSRF token so I can practice hitting the endpoints with Postman

@api_view('POST')
def create_mtg_card(request, user_id, deck_id):
  try:
    user = User.objects.get(pk=user_id)
  except User.DoesNotExist:
    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
  
  try:
    deck = Deck.objects.get(pk=deck_id)
  except Deck.DoesNotExist:
    return Response({"error": "Deck not found"}, status=status.HTTP_404_NOT_FOUND)
    
  data = request.data
  colors = data.get('colors', [])
  color_values = process_colors(colors)

  card_data = {
    "name": data.get('name'),
    "cmc": data.get('cmc'),
    "mana_cost": data.get('mana_cost'),
    "colors": ','.join(color_values),
    "type_line": data.get('type_line'),
    "rarity": data.get('rarity'),
    "cmdr_legal": data.get('cmdr_legal'),
    "img": data.get('img'),
    "purchase_uris": data.get('purchase_uris'),
  }

  serializer = CardSerializer(data=card_data)
  if serializer.is_valid():
    card = serializer.save()
    deck.deck_leader = card
    deck.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)