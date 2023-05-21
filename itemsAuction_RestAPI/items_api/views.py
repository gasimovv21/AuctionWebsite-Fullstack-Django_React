import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .utils import (
    getOwnerUsersList,
    getUsersList,
    getItemsList,
    createItem,
    getItemDetail,
    updateItem,
    deleteItem
)



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/owner_users/',
            'method': 'GET',
            'body': None,
            'description':  [
                'Retrieving all owner users from localhost:8000 => GET',
            ]
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getOwnerUsers(request):
    if request.method == 'GET':
        return getOwnerUsersList(request)


@api_view(['GET'])
def getUsers(request):
    if request.method == 'GET':
        return getUsersList(request)


@api_view(['GET', 'POST'])
def getItems(request):
    if request.method == 'GET':
        return getItemsList(request)
    
    if request.method == 'POST':
        return createItem(request)
    

@api_view(['GET', 'PUT', 'DELETE'])
def getItem(request, pk):
    
    if request.method == 'GET':
        return getItemDetail(request, pk)
    
    if request.method == 'PUT':
        return updateItem(request, pk)
    
    if request.method == 'DELETE':
        return deleteItem(request, pk)
