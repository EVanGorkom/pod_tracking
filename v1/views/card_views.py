from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from v1.utils import process_colors
from ..serializers.card_serializer import CardSerializer
from ..enums.color_enum import MtgColor
from ..models.card_model import Card
from ..models.deck_model import Deck
from ..models.user_model import User
import pdb

# This will expect a JSON package of the data we care about from the FE after the user has already chosen the 'leader' they want from the data

@api_view(['POST'])
def create_mtg_card(request, user_id, deck_id):
  try:
    deck = Deck.objects.get(pk=deck_id, user=user_id)
  except Deck.DoesNotExist:
    return Response({"error": "Deck not found"}, status=status.HTTP_404_NOT_FOUND)
  
  if deck.deck_leader == None:
    data = request.data
    colors = data.get('colors')
    color_values = process_colors(colors)

    card_data = {
      "name": data.get('name'),
      "cmc": data.get('cmc'),
      "mana_cost": data.get('mana_cost'),
      "colors": color_values,
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
  
  else:
    return Response({"error": "Deck already has a card association. Use the PUT endpoint instead."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def mtg_card_details(request, user_id, deck_id, card_id):
  try:
    deck = Deck.objects.get(pk=deck_id, user=user_id)
  except Deck.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    card = Card.objects.get(pk=card_id)
  except Card.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if card.id != deck.deck_leader.id:
    return Response({"error": "Card ID is not associated to this Deck ID."}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_card_details(card)
  elif request.method == 'PUT':
    return update_card(card, request.data)
  elif request.method == 'DELETE':
    return delete_card(card)

def get_card_details(card):
  serializer = CardSerializer(card)
  return Response(serializer.data)

def update_card(card, data):
  colors = data.get('colors')
  color_values = process_colors(colors)

  updated_card_data = {
    "name": data.get('name'),
    "cmc": data.get('cmc'),
    "mana_cost": data.get('mana_cost'),
    "colors": color_values,
    "type_line": data.get('type_line'),
    "rarity": data.get('rarity'),
    "cmdr_legal": data.get('cmdr_legal'),
    "img": data.get('img'),
    "purchase_uris": data.get('purchase_uris'),
  }
  new_card = CardSerializer(card, data=updated_card_data)
  if new_card.is_valid():
    new_card.save()
    return Response(new_card.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_card(card):
  card.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
