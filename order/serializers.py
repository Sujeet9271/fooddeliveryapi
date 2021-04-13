from rest_framework import serializers
from .models import Order,UserOrder,Delivery
from menu.serializers import MenuSerializer

class UserOrderSerializer(serializers.ModelSerializer):
    itemname = serializers.ReadOnlyField()
    class Meta:
        model = UserOrder
        fields = ['id','item','itemname','quantity','price','placed','customer','restaurant','restaurant_name','created','updated']

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
        fields = ['customer','id','itemname','quantity','price','created','updated','status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_order','restaurant','delivery','price','created','updated','status']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id','user_name','contact_number','address']
        


        
    