from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer,UserOrderSerializer

from .models import Order,UserOrder

from menu.views import res_category,sub_category,item
from menu.models import Category,Sub_Category,Menu
from menu.serializers import NestedCategorySerializer
from datetime import date

@api_view(['GET','PATCH'])
def cart(request):
    if request.method == 'GET':
        total = 0
        items = UserOrder.objects.filter(customer=request.user.id).exclude(placed=True)
        for item in items:
            total += item.price
        serializer = UserOrderSerializer(items,many=True)
        return Response({'orders':serializer.data,'total_price':total})

    if request.method == 'PATCH':
        print(request.data)
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
def create_cart(request,city,restaurant):
    if request.method == 'GET':
        print(request.user.id)
        qs=Category.objects.select_related('restaurant').filter(restaurant__city=city,restaurant=restaurant)
        serializer=NestedCategorySerializer(qs, many=True)
        return Response(serializer.data)
    else:  
        orders=request.data
        for order in orders:
            order_id = order['id']
            order_quantity = order['quantity']
            menu = Menu.objects.get(id=order_id)
            total_price = order_quantity*menu.price

            user_order = {
                'customer':1,
                'restaurant':restaurant,
                'itemname':order_id,
                'quantity':order_quantity,
                'price':total_price,
                'placed':False
            }
            serializer = UserOrderSerializer(data=user_order)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)

            
        orders = UserOrder.objects.filter(restaurant=restaurant).exclude(placed=True)
        serializer = UserOrderSerializer(orders, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def create_order(request):
    cart = UserOrder.objects.filter(customer = request.user.id).exclude(placed=True)
    serializer = UserOrderSerializer(many=True)
    for order in cart:
        staff = {
            'restaurant':order.restaurant.id,
            'status':'Pending',
            'userorder':order.id,
            'quantity':order.quantity,
            'price':order.price
        }
        print(staff)
        
        orderserializer = OrderSerializer(data=staff)
        if orderserializer.is_valid():
            orderserializer.save()
        else:
            return Response(orderserializer.errors)
    
    orders = Order.objects.filter(userorder__customer = request.user.id)
    ordersserializer = OrderSerializer(orders,many=True)

    cart = UserOrder.objects.all().update(placed=True)   

    return Response(ordersserializer.data)
    

@api_view(['GET'])
def order_received(request,city,restaurant):
    if request.user.is_staff == True:
        revenue=0
        total_order=0
        if request.method == 'GET':
            qs = Order.objects.filter(userorder__restaurant__city=city,userorder__restaurant=restaurant)
            # qs=Order.objects.filter(userorder__restaurant__city=city,userorder__restaurant=restaurant,created__year=date.today().year,created__month=date.today().month,created__day=date.today().day)
            for order in qs:
                total_order += 1
                revenue += order.userorder.price
            serializer=OrderSerializer(qs, many=True)
            return Response({'total_orders':total_order,'revenue':revenue,'orders':serializer.data})
    return Response({'ACCESS DENIED':'ACCESS DENIED'},status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','PUT','PATCH'])
def order_update(request,city,restaurant,id):
    if request.user.is_staff==True:
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
