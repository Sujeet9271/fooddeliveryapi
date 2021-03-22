from rest_framework import serializers
from .models import Order,UserOrder
from menu.serializers import MenuSerializer

class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = ['id','itemname','quantity','price','customer','restaurant']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id','restaurant','userorder','quantity','price','created','updated','status']