from rest_framework import serializers
from .models import Menu,Sub_Category,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','category','restaurant']

    # def validators(self,object):
    #     if object.category in ['']

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
        fields='__all__'

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