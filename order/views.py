from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer,UserOrderSerializer,NestedOrderSerializer,NestedUserOrderSerializer,ResOrderSerializer

from .models import Order,UserOrder

from menu.views import res_category,sub_category,item
from menu.models import Category,Sub_Category,Menu
from menu.serializers import NestedCategorySerializer
from datetime import date



@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.method == 'GET':
        total = 0
        items = UserOrder.objects.filter(customer=request.user.id).exclude(placed=True)
        for item in items:
            total += item.price
        serializer = NestedUserOrderSerializer(items,many=True)
        return Response({'orders':serializer.data,'total_price':total})

    if request.method == 'PATCH':
        for data in request.data:
            id = data['id']
            item = UserOrder.objects.get(id = id)
            id = item.itemname.id
            
            order = Menu.objects.get(id = id)
        
            new_data = {
                'id':data['id'],
                'quantity':data['quantity'],
                'price':data['quantity']*order.price
            }
            print(new_data)
            update = UserOrderSerializer(instance = item, data=new_data, partial=True)

            if update.is_valid():
                update.save()
            else:
                return Response(update.errors)

        total = 0
        items = UserOrder.objects.filter(customer=request.user.id).exclude(placed=True)
        for item in items:
            total += item.price
        serializer = UserOrderSerializer(items,many=True)
        return Response({'orders':serializer.data,'total_price':total})



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def create_cart(request,city,restaurant):
    if request.method == 'GET':
        print(request.user.is_authenticated)
        qs=Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
        serializer=NestedCategorySerializer(qs, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            orders=request.data
            for order in orders:
                order_id = order['id']
                order_quantity = order['quantity']
                menu = Menu.objects.get(id=order_id)
                total_price = order_quantity*menu.price

                user_order = {
                    'customer':request.user.id,
                    'restaurant':menu.restaurant.id,
                    'item':order_id,
                    'quantity':order_quantity,
                    'price':total_price,
                    'placed':False
                }
                print(user_order)
                serializer = UserOrderSerializer(data=user_order)

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors)

                
            orders = UserOrder.objects.filter(restaurant=restaurant).exclude(placed=True)
            serializer = UserOrderSerializer(orders, many=True)
            return Response(serializer.data)
        return Response("can't add into cart. Login First")




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart = UserOrder.objects.filter(customer = request.user.id).exclude(placed=True)
    serializer = UserOrderSerializer(many=True)
    for order in cart:
        staff = {
            'restaurant':order.restaurant.id,
            'status':'Pending',
            'user_order':order.id,
            'quantity':order.quantity,
            'price':order.price
        }
        
        
        orderserializer = OrderSerializer(data=staff)
        if orderserializer.is_valid():
            orderserializer.save()
        else:
            return Response(orderserializer.errors)
 
    cart = UserOrder.objects.all().update(placed=True)   

    return Response('Order Placed')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myorders(request):
    
    qs = Order.objects.select_related('user_order').filter(user_order__customer=request.user.id)
    serializer = NestedOrderSerializer(qs, many=True)

    total_price = 0
    for order in qs:
        total_price += order.price
    
    return Response({'orders':serializer.data,'total price':total_price})
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_received(request,city,restaurant):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        revenue=0
        total_order=0
        if request.method == 'GET':
            print(request.user)
            qs = Order.objects.filter(user_order__restaurant__city=city,user_order__restaurant=restaurant)
            # qs=Order.objects.filter(userorder__restaurant__city=city,userorder__restaurant=restaurant,created__year=date.today().year,created__month=date.today().month,created__day=date.today().day)
            for order in qs:
                total_order += 1
                revenue += order.user_order.price
            serializer=ResOrderSerializer(qs, many=True)
            return Response({'total_orders':total_order,'revenue':revenue,'orders':serializer.data})
    return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)



@api_view(['GET','PUT','PATCH'])
@permission_classes([IsAuthenticated])
def order_update(request,city,restaurant,id):
    if request.user.is_superuser or (request.user.is_staff and request.user.restaurant==restaurant):
        try:   
            order = Order.objects.get(userorder__restaurant__city=city,userorder__restaurant=restaurant,id=id)   
            serializer = OrderSerializer(order)
            if request.method == 'PATCH':
                serializer = OrderSerializer(instance = order, data=request.data, partial=True)
                # request.data['user']=request.user.id
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            if request.method=='PUT':
                serializer = OrderSerializer(instance = order, data=request.data)
                # request.data['user']=request.user.id
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
            return Response(serializer.data) 

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)
