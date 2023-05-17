from rest_framework.serializers import ModelSerializer
from .models import User, ItemInAuction


class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemInAuction
        fields = [
            'id',
            'name',
            'price',
            'item_owner',
            'created_at',
            'updated_at'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
