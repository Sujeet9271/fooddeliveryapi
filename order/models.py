from django.db import models
from django.contrib.auth.models import User
from city.models import City
from restaurant.models import Restaurant
from menu.models import Category,Menu

# Create your models here.
class UserOrder(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    itemname=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price = models.IntegerField()
    placed = models.BooleanField(default=False)


    def __str__(self):
        return f"Item={self.itemname.itemname}, Quantity={self.quantity}, Price={self.quantity*self.itemname.price}"

    class Meta:
        db_table = 'UserOrder'

        
class Order(models.Model):
    STATUS=(
        ('Pending',('Pending')),('Received',('Received')),('Placed',('Placed')),('Out for Delivery',('Out for Delivery')),('Delivered',('Delivered'))
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    userorder = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50, choices=STATUS, default='Pending')
    price = models.IntegerField()

    

    def __str__(self):
        return f"Item={self.userorder.itemname.itemname}, Quantity={self.userorder.quantity}, Price={self.userorder.quantity*self.userorder.itemname.price}"

    # @property
    # def name(self):
    #     return item.name
    
    # @property
    # def price(self,userorder,quantity):
    #     return (userorder.price*quantity)  
