from django.contrib import admin
from .models import Order,UserOrder,Delivery
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','restaurant','user_order','created', 'updated','status','customer','delivery_address')


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','restaurant','itemname','quantity','created','updated','placed')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display=('id','user','contact_number','address')
