from rest_framework.serializers import ModelSerializer
from .models import City
from restaurant.serializers import NestedRestaurantSerializer

class CitySerializer(ModelSerializer):
    class Meta:
        model=City
        fields='__all__'

class NestedCitySerializer(ModelSerializer):
    restaurant = NestedRestaurantSerializer(many=True,read_only=True)

    class Meta:
        model = City
        fields = ['id','name','pincode','restaurant']
