from django.contrib import admin
from .models import Order,UserOrder
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','restaurant','user_order','created', 'updated','status','customer','delivery_address')


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','restaurant','itemname','quantity','created','updated','placed')

