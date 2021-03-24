from django.db import models
from accounts.models import User
from city.models import City
from restaurant.models import Restaurant
from menu.models import Category,Menu

# Create your models here.
class UserOrder(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    item=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='menu_item')
    quantity=models.IntegerField(default=1)
    price = models.IntegerField()
    placed = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item={self.item.itemname}, Quantity={self.quantity}, Price={self.quantity*self.item.price}"

    class Meta:
        ordering=['-updated']
        db_table = 'UserOrder'

        
class Order(models.Model):
    STATUS=(
        ('Pending',('Pending')),('Received',('Received')),('Placed',('Placed')),('Out for Delivery',('Out for Delivery')),('Delivered',('Delivered'))
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE,related_name='user_order')
    quantity = models.IntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50, choices=STATUS, default='Pending')
    price = models.IntegerField()

    
    class Meta:
        ordering=['-updated']
        db_table='Order'

    def __str__(self):
        return f"Item={self.user_order.item.itemname}, Quantity={self.user_order.quantity}, Price={self.user_order.quantity*self.user_order.item.price}"
 
