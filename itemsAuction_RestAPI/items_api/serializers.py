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
    
    # def to_representation(self, instance):
    #     rep = super(ItemSerializer, self).to_representation(instance)
    #     rep['item_owner'] = instance.item_owner.name
    #     return rep


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
