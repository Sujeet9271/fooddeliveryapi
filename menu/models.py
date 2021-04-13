from django.db import models
from django.core.exceptions import ValidationError

from restaurant.models import Restaurant

# Create your models here.
class Category(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='category')
    category=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category} ({self.restaurant})"

    class Meta:
        db_table='Category'

    def clean(self):
        if self.restaurant.veg_only==True and self.category.lower() in ['nonveg','non veg','non-veg']:
            raise ValidationError(f"{self.restaurant} cannot have Non-Vegetarian Items")

    def restaurant_name(self):
        return self.restaurant.name




class Sub_Category(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='sub_category')
    sub_category=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sub_category}({self.category})"
    
    class Meta:
        db_table='Sub_Category'

    def clean(self):
        if self.category.restaurant.veg_only==True and self.sub_category.lower() in ['nonveg','non veg','non-veg']:
            raise ValidationError(f"{self.category.restaurant} cannot have Non-Vegetarian Items")

    def restaurant_name(self):
        return self.category.restaurant_name()

def location(instance,filename):
    return f"{instance.restaurant.city}/{instance.restaurant.name}/menu/{filename}"

class Menu(models.Model):
    STATUS = (
        ('Unrated',('Unrated')),
       ('Bad', ('Bad')),
       ('Satisfactory',('Satisfactory')),
       ('Good', ('Good')),
       ('Excellent', ('Excellent')),
    )
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category=models.ForeignKey(Sub_Category, on_delete=models.CASCADE,related_name='menu')
    itemname=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    description = models.TextField(null=True,blank=True)
    rating=models.CharField(max_length=50,choices=STATUS,null=True,default='Unrated')
    image = models.ImageField(null=True,blank=True,upload_to=location)

    def __str__(self):
        return f"{self.itemname}({self.category.category}) from {self.restaurant}"
    
    class Meta:
        db_table='Menu'

    def restaurant_name(self):
        return self.restaurant.name

    def category_name(self):
        return self.category.category

    def subcategory_name(self):
        return self.sub_category.sub_category

