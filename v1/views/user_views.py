from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.user_model import User
from ..serializers.user_serializer import UserSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        return get_user_list(request)
    elif request.method == 'POST':
        return create_user(request)
    
def get_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get_user_details(User)
    elif request.method == 'PUT':
        return update_user(User, request.data)
    elif request.method == 'DELETE':
        return delete_user(User)

def get_user_details(user):
    serializer = UserSerializer(user)
    return Response(serializer.data)

def update_user(user, data):
    user_data = UserSerializer(user, data=data, partial=True)
    if user_data.is_valid():
        user_data.save()
        return Response(user_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_user(user):
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
