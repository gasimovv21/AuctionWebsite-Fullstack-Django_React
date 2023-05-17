import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .utils import getOwnerUsersList


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