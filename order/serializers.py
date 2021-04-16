from rest_framework import serializers
from .models import Order,UserOrder
from menu.serializers import MenuSerializer
from menu.models import Menu

class UserOrderSerializer(serializers.ModelSerializer):
    itemname = serializers.ReadOnlyField()
    class Meta:
        model = UserOrder
        fields = ['id','item','itemname','image','quantity','price','placed','customer','restaurant','restaurant_name','created','updated']


class ResOrderSerializer(serializers.ModelSerializer):
    itemname = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['customer','id','itemname','image','quantity','price','created','updated','status','delivery_address']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_order','image','restaurant','price','created','updated','status','address','contact_number']

class MyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_order','image','restaurant','price','created','status','delivery_address']



        
    