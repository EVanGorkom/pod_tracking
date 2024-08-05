from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.user_model import User
from ..models.deck_model import Deck
from ..serializers.user_serializer import UserSerializer
from ..serializers.deck_serializer import DeckSerializer

@api_view(['GET', 'POST'])
def deck_list(request, user_id):
    try:
        check_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_deck_list(request, check_user)
    elif request.method == 'POST':
        return create_deck(request)

def get_deck_list(request, check_user):
    decks = Deck.objects.filter(user=check_user)
    serializer = DeckSerializer(decks, many=True)
    return Response(serializer.data)

def create_deck(request):
    serializer = DeckSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def deck_details(request, user_id, deck_id):
    try:
        user = user.objects.get(pk=user_id)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    try:
        deck = deck.objects.get(pk=deck_id, user=user)
    except deck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_deck_details(deck)
    elif request.method == 'PUT':
        return update_deck(deck, request.data)
    elif request.method == 'DELETE':
        return delete_deck(deck)

def get_deck_details(deck):
    serializer = DeckSerializer(deck)
    return Response(serializer.data)

def update_deck(deck, data):
    deck_data = DeckSerializer(deck, data=data, partial=True)
    if deck_data.is_valid():
        deck_data.save()
        return Response(deck_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_deck(deck):
    deck.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

