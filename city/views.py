from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CitySerializer,NestedCitySerializer
from .models import City
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_city(request):
    try:
        qs=City.objects.all()
        serializer=NestedCitySerializer(qs,many=True)
        return Response(serializer.data)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def city(request):
    try:
        qs=City.objects.all()
        serializer=CitySerializer(qs,many=True)
        return Response(serializer.data)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def search(request):
    if request.method=='POST':
        try:
            city=request.data['city']
            qs=City.objects.filter(name=city)
            serializer=CitySerializer(qs,many=True)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def index(request):
    context={
        'message':'WELCOME TO FOOD DELIVERY API',
        'DETAILED VIEW':"http://127.0.0.1:8000/detail/cities/ [name='detail_city']",
        'Cities':"http://127.0.0.1:8000/cities/ [name='city']",
        'Restaurants':"http://127.0.0.1:8000/cities/<int:city>/",
        'Menu/create order':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/",
        'restaurant_category':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/",
        'restaurant_category_detail':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/",
        'restaurant_category_subcategory':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/",
        'restaurant_category_subcategory_detail':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/",
        'restaurant_category_subcategory_items':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/item/",
        'restaurant_category_subcategory_item_detail':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/category/<int:category>/subcategory/<int:subcategory>/item/<int:item>/",
        'orders received':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/orders/ ",
        'update order':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/orders/<int:id>/",
        'restaurant_menu':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/orders/<int:id>/",
        'restaurant_category':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/",
        'update category':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/update/",
        'subcategory':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/",
        'update_subcategory':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/",
        'add menu item':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/item/",
        'update_subcategory_item_detail':"http://127.0.0.1:8000/cities/<int:city>/restaurant/<int:restaurant>/staff/menu/category/<int:category>/subcategory/<int:subcategory>/item/<int:item>/",

        }
    return Response(context)


# detail/http://127.0.0.1:8000/cities/<int:city>/ [name='detailed_restaurants']
                            

                              