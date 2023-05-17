from django.contrib import admin
from .models import ItemInAuction, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'email',
    )
    list_filter = (
        'id',
        'name',
        'email',
        'created_at',
        'updated_at',
    )
    empty_value_display = '-empty-'

@admin.register(ItemInAuction)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'item_owner',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'price',
        'item_owner',
    )
    list_filter = (
        'id',
        'name',
        'price',
        'item_owner',
        'created_at',
        'updated_at',
    )
    empty_value_display = '-empty-'
