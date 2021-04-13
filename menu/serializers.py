from rest_framework import serializers
from .models import Menu,Sub_Category,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','category','restaurant']

    def validate(self, attrs):
        instance = Category(**attrs)
        instance.clean()
        return attrs

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Sub_Category
        fields=['id','sub_category','category']

    def validate(self, attrs):
        instance = Sub_Category(**attrs)
        instance.clean()
        return attrs

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['id','itemname','description','price','rating','restaurant','category','sub_category','restaurant_name','category_name','subcategory_name']

class NestedSubCategorySerializer(serializers.ModelSerializer):
    
    menu=MenuSerializer(many=True,read_only=True)

    class Meta:
        model = Sub_Category
        fields=['id','category','sub_category','menu']
     

class NestedCategorySerializer(serializers.ModelSerializer):

    sub_category=NestedSubCategorySerializer(many=True,read_only=True)

    class Meta:
        model=Category
        fields=['id','category','sub_category']