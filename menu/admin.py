from django.contrib import admin
from .models import Category,Menu,Sub_Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category']

@admin.register(Sub_Category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['id','sub_category','category']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','itemname','sub_category','price','quantity'] 