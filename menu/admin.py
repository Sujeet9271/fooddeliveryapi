from django.contrib import admin
from .models import Category,Menu,Sub_Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category','restaurant_name']

@admin.register(Sub_Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['id','sub_category','category','restaurant_name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','itemname','price','description','sub_category','category','restaurant'] 