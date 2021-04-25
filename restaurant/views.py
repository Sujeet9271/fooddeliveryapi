from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import RestaurantSerializer,NestedRestaurantSerializer,RestaurantRatingSerializer
from .models import Restaurant,RestaurantRating
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant(request,city):
    try:
        qs=Restaurant.objects.filter(city=city)
        serializer=RestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def veg_restaurant(request,city):
    try:
        qs=Restaurant.objects.select_related('city').filter(veg_only=True)
        serializer=RestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detailed_restaurant(request,city):
    try:
        qs=Restaurant.objects.filter(city=city)
        serializer=NestedRestaurantSerializer(qs,many=True)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST','PATCH'])
def rate_restaurant(request,city,restaurant):
    try:
        restaurant = Restaurant.objects.get(id=restaurant)    
        if request.method == 'GET':
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        elif request.method == 'POST':
            rating = request.data['rating']
            # r = {
            #     'user':request.user,
            #     'restaurant':restaurant,
            #     'rating':request.data['rating']
            # }
            restaurant_rating = RestaurantRating.objects.create(user=request.user,restaurant=restaurant,rating=rating)
            restaurant_rating.save()
            return Response('rated')
        elif request.method == 'PATCH':
            rating = request.data['rating']
            restaurant_rating = RestaurantRating.objects.filter(user=request.user,restaurant=restaurant).update(rating=rating)
            return Response('rated')
    except Restaurant.DoesNotExist:
        return Response('Restaurant Doesnot Exist',status=status.HTTP_404_NOT_FOUND)