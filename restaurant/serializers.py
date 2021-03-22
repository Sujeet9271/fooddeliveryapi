from rest_framework.serializers import ModelSerializer
from .models import Restaurant
from menu.serializers import NestedCategorySerializer

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model =  Restaurant
        fields='__all__'

class NestedRestaurantSerializer(ModelSerializer):
    category=NestedCategorySerializer(many=True,read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id','name','phnumber','address','rating','category']
        