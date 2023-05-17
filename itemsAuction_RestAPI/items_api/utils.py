import requests


from rest_framework.response import Response
from .models import User, ItemInAuction
from .serializers import UserSerializer


def getOwnerUsersList(request):
    url = 'http://127.0.0.1:8000/api/users/'
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        for user_data in users:
            # Проверяем, существует ли пользователь с таким email
            existing_user = User.objects.filter(email=user_data['email']).first()

            if existing_user:
                # Проверяем, отличается ли поле name
                if existing_user.name != user_data['name']:
                    existing_user.name = user_data['name']

                # Проверяем, отличается ли поле created_at
                if existing_user.created_at != user_data['created_at']:
                    existing_user.created_at = user_data['created_at']

                # Проверяем, отличается ли поле updated_at
                if existing_user.updated_at != user_data['updated_at']:
                    existing_user.updated_at = user_data['updated_at']

                existing_user.save()
            else:
                user = User(
                    name=user_data['name'],
                    email=user_data['email'],
                    created_at=user_data['created_at'],
                    updated_at=user_data['updated_at'],
                )
                user.save()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    else:
        err = 'Error in process of getting users: ' + str(response.status_code)
        print(err)
        return Response({'error': err}, status=500)