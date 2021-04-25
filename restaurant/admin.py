from django.contrib import admin
from .models import Restaurant,RestaurantRating
# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=['id','name','phnumber','address','city','status','veg_only','rating_average','review_count']
    list_filter=['city']

@admin.register(RestaurantRating)
class Rating(admin.ModelAdmin):
    list_display=['id','restaurant','user','rating']
    list_filter=['restaurant','rating']
    
    