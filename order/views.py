from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer,UserOrderSerializer,ResOrderSerializer,MyOrderSerializer

from .models import Order,UserOrder
from accounts.serializers import ProfileSerializer
from accounts.models import Profile

from menu.views import res_category,sub_category,item
from menu.models import Category,Sub_Category,Menu
from menu.serializers import NestedCategorySerializer
from datetime import date




@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def create_cart(request,city,restaurant):
    if request.method == 'GET':
        qs=Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
        serializer=NestedCategorySerializer(qs, many=True)
        return Response(serializer.data)
    else:
        orders=request.data
        for order in orders:
            order_id = order['id']
            order_quantity = order['quantity']
            menu = Menu.objects.get(id=order_id)

            user_order = {
                'customer':request.user.id,
                'restaurant':menu.restaurant.id,
                'item':order_id,
                'quantity':order_quantity,
                'placed':False
            }
            serializer = UserOrderSerializer(data=user_order)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)
        return Response('Added To Cart')


@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.method == 'GET':
        total = 0
        items = UserOrder.objects.filter(customer=request.user.id).exclude(placed=True)
        for item in items:
            total += item.price()
        serializer = UserOrderSerializer(items,many=True)
        return Response({'orders':serializer.data,'total_price':total})

    if request.method == 'PATCH':
        for data in request.data:
            item = UserOrder.objects.get(id = data['id'])
            
            order = Menu.objects.get(id = item.item.id)
        
            new_data = {
                'id':data['id'],
                'quantity':data['quantity'],
            }
            update = UserOrderSerializer(instance = item, data=new_data, partial=True)

            if update.is_valid():
                update.save()
            else:
                return Response(update.errors)

        total = 0
        items = UserOrder.objects.filter(customer=request.user.id).exclude(placed=True)
        for item in items:
            total += item.price()
        serializer = UserOrderSerializer(items,many=True)
        return Response({'orders':serializer.data,'total_price':total})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_delete(request,id):
    try:
        item = UserOrder.objects.get(id=id)
        item.delete()
        return Response('item deleted')
    except UserOrder.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    
    if request.method=='GET':
        cart = UserOrder.objects.filter(customer = request.user.id).exclude(placed=True)
        items = UserOrderSerializer(cart,many=True)
        try:
            user = Profile.objects.get(user = request.user)
            address = ProfileSerializer(user)
            return Response({'address':address.data,'cart':items.data})
        except Profile.DoesNotExist:
            return Response({'address':'','cart':items.data})
    elif request.method=='POST':   
        user = Profile.objects.get(user = request.user)
        address = user.address
        contact_number = user.contact_number     
        if request.data:
            address = address if request.data['address'] == '' else request.data['address'] 
            contact_number =  contact_number if request.data['contact_number']== '' else request.data['contact_number']
        else:
            user = Profile.objects.get(user=request.user)
            address = user.address
            contact_number = user.contact_number

        cart = UserOrder.objects.select_related('customer').filter(customer = request.user.id).exclude(placed=True).exists()
        if cart:
            for order in UserOrder.objects.select_related('customer').filter(customer = request.user.id).exclude(placed=True):
                item = {
                    'restaurant':order.restaurant.id,
                    'status':'Pending',
                    'user_order':order.id,
                    'address':address,
                    'contact_number':contact_number
                }
                
                
                orderserializer = OrderSerializer(data=item)
                if orderserializer.is_valid():
                    orderserializer.save()
                else:
                    return Response(orderserializer.errors)

            cart = UserOrder.objects.filter(customer = request.user.id).update(placed=True) 
            return Response('Order Placed')
        else:
            return Response('Cart is Empty')
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myorders(request):    
    qs = Order.objects.select_related('user_order').filter(user_order__customer=request.user.id)    
    serializer = MyOrderSerializer(qs, many=True)

    total_price = 0
    total_item = 0
    for order in qs:
        total_price += order.user_order.price()
        total_item+=1
    
    return Response({'orders':serializer.data,'total_price':[total_price],'total_item':total_item})
    




# For Restaurant----------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def order_received(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        revenue=0
        total_order=0
        if request.method == 'GET':
            qs = Order.objects.filter(restaurant=restaurant)
            for order in qs:
                total_order += 1
                revenue += order.user_order.price()
            serializer=ResOrderSerializer(qs, many=True)
            return Response({'total_orders':[total_order],'revenue':[revenue],'orders':serializer.data})
        elif request.method == 'PATCH':
            try:
                id=request.data['id']   
                order = Order.objects.get(restaurant=restaurant,restaurant__city=city,id=id)   
                serializer = OrderSerializer(instance = order, data=request.data, partial=True)                    
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except Order.DoesNotExist:
                return Response('NOT Found',status=status.HTTP_404_NOT_FOUND)
    return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def new_order_received(request):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant!=0):
        print(request.user.restaurant)
        revenue=0
        total_order=0
        if request.method == 'GET':
            qs = Order.objects.filter(restaurant=request.user.restaurant)
            for order in qs:
                total_order += 1
                revenue += order.user_order.price()
            serializer=ResOrderSerializer(qs, many=True)
            return Response({'total_orders':[total_order],'revenue':[revenue],'orders':serializer.data})
        elif request.method == 'PATCH':
            try:
                id=request.data['id']   
                order = Order.objects.get(restaurant=request.user.restaurant,id=id)   
                serializer = OrderSerializer(instance = order, data=request.data, partial=True)                    
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except Order.DoesNotExist:
                return Response('NOT Found',status=status.HTTP_404_NOT_FOUND)
    return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def order_update(request,city,restaurant,id):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        try:   
            order = Order.objects.get(restaurant=restaurant,restaurant__city=city,id=id)   
            serializer = OrderSerializer(order)
            if request.method == 'PATCH':
                serializer = OrderSerializer(instance = order, data=request.data, partial=True)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data) 

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)