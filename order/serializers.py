from rest_framework import serializers
from .models import Order,UserOrder
from menu.serializers import MenuSerializer

class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = ['id','item','quantity','price','created','placed','customer']

class NestedUserOrderSerializer(serializers.ModelSerializer):

    menu_item=MenuSerializer(many=True,read_only=True)

    class Meta:
        model = UserOrder
        fields = ['id','item','menu_item','quantity','price','created','placed','customer']
        depth=1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','restaurant','user_order','quantity','price','created','updated','status']


class NestedOrderSerializer(serializers.ModelSerializer):

    # Order = (many=True,read_only=True)

    class Meta:
        model = Order
        fields = ['id','user_order','created','updated','status']
        depth=1
        
    