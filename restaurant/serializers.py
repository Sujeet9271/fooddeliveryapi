from rest_framework.serializers import ModelSerializer
from .models import Restaurant,RestaurantRating
from menu.serializers import NestedCategorySerializer

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model =  Restaurant
        fields=['id','name','address','phnumber','status','image','rating_average','review_count','veg_only','image']

class RestaurantRatingSerializer(ModelSerializer):
    class Meta:
        model =  RestaurantRating
        fields='__all__'

class NestedRestaurantSerializer(ModelSerializer):
    category=NestedCategorySerializer(many=True,read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id','name','address','phnumber','status','image','rating_average','review_count','veg_only','category']

class RestaurantRatingSerializer(ModelSerializer):
    class Meta:
        model = RestaurantRating
        fields = ['id','user','restaurant_name','rating']
        