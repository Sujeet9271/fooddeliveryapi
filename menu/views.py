from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import MenuSerializer,SubCategorySerializer,CategorySerializer,NestedSubCategorySerializer,NestedCategorySerializer
from .models import Menu,Sub_Category,Category,Rating
from order.serializers import OrderSerializer,UserOrderSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_menu(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method == 'GET':
            qs=Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
            serializer=NestedCategorySerializer(qs, many=True)
            return Response(serializer.data)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_category(request,city,restaurant):
    try:
        category = Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
        serializer = NestedCategorySerializer(category,many=True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_category_subcategory(request,city,restaurant,category):
    try:
        subcategory = Sub_Category.objects.select_related('category').filter(category=category)
        serializer = NestedSubCategorySerializer(subcategory,many=True)
        print(serializer.data)
        return Response(serializer.data)
    except Sub_Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_category_subcategory_detail(request,city,restaurant,category,subcategory):
    try:
        subcategory = Sub_Category.objects.select_related('category').filter(category=category,id=subcategory)
        serializer = NestedSubCategorySerializer(subcategory,many=True)
        print(serializer.data)
        return Response(serializer.data)
    except Sub_Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_category_detail(request,city,restaurant,category):
    try:
        category = Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant,id=category)
        serializer = NestedCategorySerializer(category,many=True)
        print(serializer.data)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_menu(request,city,restaurant,category,subcategory):
    try:
        qs=Menu.objects.select_related('sub_category').filter(restaurant__city=city,restaurant=restaurant,category=category,sub_category=subcategory)
        serializer=MenuSerializer(qs, many=True)
        return Response(serializer.data)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurant_category_subcategory_item_detail(request,city,restaurant,category,subcategory,item):
    try:
        item = Menu.objects.get(sub_category=subcategory,id=item)
        serializer = MenuSerializer(item)
        return Response(serializer.data)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def res_category(city,restaurant):
    categories = Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
    return categories

def sub_category(city,restaurant,category):
    return Sub_Category.objects.select_related('category').filter(category=category)





@api_view(['GET','POST','PATCH'])
def rate_item(request,city,restaurant,id):
    item = Menu.objects.get(id=id)
    if request.method == 'GET':
        serializer = MenuSerializer(item)
        return Response(serializer.data)
    elif request.method == 'POST':
        rating = request.data['rating']
        item_rating = Rating.objects.create(user=request.user,item=item,rating=rating)
        item_rating.save()
        return Response('rated')
    elif request.method == 'PATCH':
        rating = request.data['rating']
        item_rating = Rating.objects.filter(user=request.user,item=item).update(rating=rating)
        return Response('rated')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def category(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method == 'GET':
            qs=Category.objects.filter(restaurant__city=city,restaurant=restaurant)
            serializer=CategorySerializer(qs, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            new={
                'restaurant':restaurant,'category':request.data['category']
            }
            serializer = CategorySerializer(data=new)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)

@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def update_category(request,city,restaurant,category):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        qs=Category.objects.get(id=category)
        print(category,qs.category,qs.restaurant.id)
        if request.method == 'GET':
            serializer=CategorySerializer(qs)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            qs.delete()
            return Response('Deleted')
        elif request.method == 'PATCH':
            print(request.data)
            serializer = CategorySerializer(instance = qs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        elif request.method=='PUT':
            serializer = CategorySerializer(instance = qs, data=request.data)
            request.data['restaurant']=restaurant
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def subcategory(request,city,restaurant,category):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method == 'GET':
            qs=Sub_Category.objects.filter(category__restaurant__city=city,category__restaurant=restaurant,category=category)
            serializer=SubCategorySerializer(qs,many=True)
            return Response(serializer.data)
        if request.method == 'POST':    
            serializer = SubCategorySerializer(data=request.data)        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)

@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def update_subcategory(request,city,restaurant,category,subcategory):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        qs=Sub_Category.objects.get(id=subcategory,category=category)
        if request.method == 'GET':
            serializer=SubCategorySerializer(qs)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            qs.delete()
            return Response('Deleted')
        elif request.method == 'PATCH':
            serializer = SubCategorySerializer(instance = qs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        elif request.method=='PUT':
            serializer = SubCategorySerializer(instance = qs, data=request.data)
            request.data['category']=category
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def add_item(request,city,restaurant,category,subcategory):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method == 'GET':
            qs=Menu.objects.filter(sub_category=subcategory,category__restaurant=restaurant,category__restaurant__city=city)
            serializer=MenuSerializer(qs, many=True)
            return Response(serializer.data)
        elif request.method=='POST':
            print(request.data)
            new={
                'itemname':request.data['itemname'],
                'category':category,
                'sub_category':subcategory,
                'price':request.data['price'],
                'description':request.data['description'],
                'restaurant':restaurant,
                'available':request.data['available'],
                'image':request.data['image']
            }
            serializer = MenuSerializer(data=new)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)

@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def update_item(request,city,restaurant,category,subcategory,item):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        try:
            item = Menu.objects.get(sub_category=subcategory,id=item)   
            if request.method == 'PATCH':
                print(request.data)
                serializer = MenuSerializer(instance = item, data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            elif request.method=='PUT':
                serializer = MenuSerializer(instance = item, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
            elif request.method == 'DELETE':
                item.delete()
                return Response('Item Deleted')
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response('Item Not Found',status=status.HTTP_404_NOT_FOUND)
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)


@api_view((['GET','POST','DELETE']))
def allitems(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method=='GET':
            qs1=Sub_Category.objects.select_related('category').filter(category__restaurant=restaurant)
            subcategory = SubCategorySerializer(qs1,many=True)
            qs2 = Category.objects.select_related('restaurant').filter(restaurant=restaurant)
            category = CategorySerializer(qs2,many=True)
            qs=Menu.objects.select_related('restaurant').filter(restaurant=restaurant)
            serializer = MenuSerializer(qs,many=True)
            return Response({'items':serializer.data,'category':category.data,'subcategory':subcategory.data})    
        elif request.method == 'POST':
            new={
                'itemname':request.data['itemname'],
                'category':request.data['category'],
                'sub_category':request.data['sub_category'],
                'price':request.data['price'],
                'description':request.data['description'],
                'restaurant':restaurant,
                'image':request.data['image'],
                'available':request.data['available']
            }
            serializer = MenuSerializer(data=new)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)



@api_view((['GET','POST']))
def allsub(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        if request.method=='GET':
            qs1=Sub_Category.objects.select_related('category').filter(category__restaurant=restaurant)
            subcategory = SubCategorySerializer(qs1,many=True)
            qs2 = Category.objects.select_related('restaurant').filter(restaurant=restaurant)
            category = CategorySerializer(qs2,many=True)
            return Response({'category':category.data,'subcategory':subcategory.data})     

        if request.method == 'POST':    
            serializer = SubCategorySerializer(data=request.data)        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)              
    return Response('ACCESS DENIED',status=status.HTTP_403_FORBIDDEN)