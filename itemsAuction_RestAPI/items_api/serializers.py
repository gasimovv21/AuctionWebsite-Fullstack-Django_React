from rest_framework import serializers
from .models import User, ItemInAuction


class ItemSerializer(serializers.ModelSerializer):
    item_owner = serializers.CharField(source='item_owner.name')

    class Meta:
        model = ItemInAuction
        fields = '__all__'

    def update(self, instance, validated_data):
        item_owner_name = validated_data.pop('item_owner', None)
        print(item_owner_name['name'])
        if item_owner_name:
            item_owner = User.objects.get(name=item_owner_name['name'])
            instance.item_owner = item_owner

        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        rep = super(ItemSerializer, self).to_representation(instance)
        rep['item_owner'] = instance.item_owner.name
        return rep


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
