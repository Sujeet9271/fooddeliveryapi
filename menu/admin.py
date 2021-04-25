from django.contrib import admin
from .models import Category,Menu,Sub_Category,Rating
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category','restaurant_name']
    list_filter=['restaurant']

@admin.register(Sub_Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['id','sub_category','category','restaurant_name']
    list_filter=['category']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','itemname','price','description','sub_category','category','restaurant','review_count','rating_average'] 
    list_filter=['sub_category','category']

@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display=['id','user','item','rating'] 
    list_filter=['rating']


