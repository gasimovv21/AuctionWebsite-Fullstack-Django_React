from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import (
    getUserDetail,
    updateUser,
    deleteUser,
    getUsersList,
    createUser
)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/users/',
            'method': [
                'GET',
                'POSTS'
            ],
            'body': None,
            'description':  [
                'Retrieving all users => GET',
                'Adding a user => POST'
            ]
        },
        {
            'Endpoint': 'users/id',
            'method': [
                'GET',
                'PUT',
                'DELETE'
            ],
            'body': None,
            'description':  [
                'Retrieving user information => GET',
                'Editing a user => PUT',
                'Deleting a user => DELETE'
            ]
        },
    ]
    return Response(routes)



@api_view(['GET', 'POST'])
def getUsers(request):
    if request.method == 'GET':
        return getUsersList(request)
    
    if request.method == 'POST':
        return createUser(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getUser(request, pk):
    
    if request.method == 'GET':
        return getUserDetail(request, pk)
    
    if request.method == 'PUT':
        return updateUser(request, pk)
    
    if request.method == 'DELETE':
        return deleteUser(request, pk)
