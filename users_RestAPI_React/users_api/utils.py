import requests


from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


url = 'http://127.0.0.1:8001/api/owner_users/'


def getUsersList(request):
    users = User.objects.all().order_by('-updated_at')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def createUser(request):
    data = request.data
    user = User.objects.create(
        name = data['name'],
        email = data['email']
    )
    serializer = UserSerializer(user, many=False)

    if serializer:
        requests.get(url)
    return Response(serializer.data)

def getUserDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()
        requests.get(url)

    return Response(serializer.data)


def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    requests.get(url)
    return Response('User was deleted sucessfully!')
