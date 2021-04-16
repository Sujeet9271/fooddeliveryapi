from django.db import models
from accounts.models import User
from city.models import City
from restaurant.models import Restaurant
from menu.models import Category,Menu

# Create your models here.

class UserOrder(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer')
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='restaurant')
    item=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='cart_item')
    quantity=models.PositiveIntegerField(default=1)
    placed = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Item={self.item.itemname}, Quantity={self.quantity}, Price={self.quantity*self.item.price}"

    class Meta:
        ordering=['-updated']
        db_table = 'UserOrder'
    
    def itemname(self):
        return f"{self.item.itemname}-{self.item.category.category}"

    def image(self):
        return self.item.image.url
    
    def restaurant_name(self):
        return self.restaurant.name

    def price(self):
        return (self.quantity*self.item.price)

    def customer_name(self):
        if 'None' in self.customer.get_full_name().split(' '):
            return self.customer.get_short_name()
        return self.customer.get_full_name()
    


def user_address(instance):
    return instance.user_order.customer.profile.address

def user_contact(instance):
    return instance.user_order.customer.profile.contact_number
        
class Order(models.Model):
    STATUS=(
        ('Pending',('Pending')),('Received',('Received')),('Placed',('Placed')),('Out for Delivery',('Out for Delivery')),('Delivered',('Delivered'))
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE,related_name='order')
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50, choices=STATUS, default='Pending')
    address = models.TextField(default=user_address)
    contact_number = models.CharField(max_length=10,default=user_contact)

    
    class Meta:
        ordering=['-updated']
        db_table='Order'

    def __str__(self):
        return f"Item={self.user_order.item.itemname}, Quantity={self.user_order.quantity}, Price={self.user_order.quantity*self.user_order.item.price}"

    def itemname(self):
        return self.user_order.item.itemname
    
    def image(self):
        return self.user_order.item.image.url

    def customer(self):
        if 'None' in self.user_order.customer.get_full_name().split(' '):
            return self.user_order.customer.get_short_name()
        return self.user_order.customer.get_full_name()

    def price(self):
        return(self.user_order.price())

    def quantity(self):
        return self.user_order.quantity

    def delivery_address(self):
        return self.address

    
    

 
