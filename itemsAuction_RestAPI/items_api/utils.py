import requests

from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import User, ItemInAuction
from .serializers import UserSerializer, ItemSerializer


def getOwnerUsersList(request):
    url = 'http://127.0.0.1:8000/api/users/'
    response = requests.get(url)

    if response.status_code == 200:
        users_data = response.json()
        existing_emails = User.objects.values_list('email', flat=True)

        User.objects.exclude(email__in=[user_data['email'] for user_data in users_data]).delete()

        for user_data in users_data:
            email = user_data['email']
            existing_user = User.objects.filter(email=email).first()

            if existing_user:
                if existing_user.name != user_data['name']:
                    existing_user.name = user_data['name']

                if existing_user.created_at != user_data['created_at']:
                    existing_user.created_at = user_data['created_at']

                if existing_user.updated_at != user_data['updated_at']:
                    existing_user.updated_at = user_data['updated_at']

                existing_user.save()
            else:
                user = User(
                    name=user_data['name'],
                    email=email,
                    created_at=user_data['created_at'],
                    updated_at=user_data['updated_at'],
                )
                user.save()

        users = User.objects.filter(email__in=[user_data['email'] for user_data in users_data])
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    else:
        err = 'Error in the process of getting users: ' + str(response.status_code)
        print(err)
        return Response({'error': err}, status=500)


def getUsersList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

def getItemsList(request):
    items = ItemInAuction.objects.all().order_by('-updated_at')
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


def createItem(request):
    data = request.data
    
    item_owner = data['item_owner']
    try:
        item_owner = get_object_or_404(User, name=item_owner)
    except Http404:
        return Response(f"Item owner not found. Check which users is available: http://127.0.0.1:8001/api/owner_users/", status=status.HTTP_404_NOT_FOUND)
    try:
        item = ItemInAuction.objects.create(
            name=data['name'],
            price=data['price'],
            item_owner=item_owner,
        )
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)
    except IntegrityError:
        return Response("Item name already exists", status=status.HTTP_409_CONFLICT)


def getItemDetail(request, pk):
    items = ItemInAuction.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)


def updateItem(request, pk):
    data = request.data
    item = ItemInAuction.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)



def deleteItem(request, pk):
    item = ItemInAuction.objects.get(id=pk)
    item.delete()
    return Response('User was deleted sucessfully!')

