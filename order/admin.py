from django.contrib import admin
from .models import Order,UserOrder
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','restaurant','user_order','created', 'updated','status','customer','delivery_address')
    list_filter=['restaurant','created','updated','status']
    list_per_page=10
    fieldsets = (
        ('Order', {'fields': ('restaurant', 'user_order','status')}),
        ('Delivery info', {'fields': ('address','contact_number')}),
        
    )


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','restaurant','itemname','quantity','created','updated','placed')
    list_filter=['restaurant','customer','created','updated','placed']
    list_per_page=10
    fieldsets = (
        ('Order', {'fields': ('restaurant','customer','item','quantity','placed')}),       
        
    )
    
