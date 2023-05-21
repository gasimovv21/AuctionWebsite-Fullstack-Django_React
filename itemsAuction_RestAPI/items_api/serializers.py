from rest_framework import serializers
from .models import User, ItemInAuction


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemInAuction
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     rep = super(ItemSerializer, self).to_representation(instance)
    #     rep['item_owner'] = instance.item_owner.name
    #     return rep


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
