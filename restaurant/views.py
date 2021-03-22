from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import RestaurantSerializer,NestedRestaurantSerializer
from .models import Restaurant
# Create your views here.

@api_view(['GET'])
def restaurant(request,city):
    try:
        qs=Restaurant.objects.filter(city=city)
        serializer=RestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def veg_restaurant(request,city):
    try:
        qs=Restaurant.objects.select_related('city').filter(veg_only=True)
        serializer=RestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def detailed_restaurant(request,city):
    try:
        qs=Restaurant.objects.filter(city=city)
        serializer=NestedRestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)