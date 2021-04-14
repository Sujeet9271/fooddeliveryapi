from rest_framework import serializers
from .models import Order,UserOrder,Delivery
from menu.serializers import MenuSerializer
from menu.models import Menu

class UserOrderSerializer(serializers.ModelSerializer):
    itemname = serializers.ReadOnlyField()
    class Meta:
        model = UserOrder
        fields = ['id','item','itemname','image','quantity','price','placed','customer','restaurant','restaurant_name','created','updated','address']

# class CartSerializer(serializers.ModelSerializer):
#     cart_item = UserOrderSerializer(many=True,read_only=True)

#     class Meta:
#         model = Menu
#         fields = ['image','cart_item']

# class NestedUserOrderSerializer(serializers.ModelSerializer):
#     itemname = serializers.ReadOnlyField()
#     image = serializers.ReadOnlyField()

#     class Meta:
#         model = UserOrder
#         fields = ['id','item','itemname','image','quantity','price','created','placed','customer']


class ResOrderSerializer(serializers.ModelSerializer):
    itemname = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['customer','id','itemname','image','quantity','price','created','updated','status','delivery_address']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_order','image','restaurant','price','created','updated','status']

class MyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_order','image','restaurant','price','created','status','delivery_address']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id','user_name','contact_number','address']
        


        
    