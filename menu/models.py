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


class Sub_Category(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='sub_category')
    sub_category=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sub_category}({self.category} from {self.category.restaurant})"
    
    class Meta:
        db_table='Sub_Category'

    def clean(self):
        if self.category.restaurant.veg_only==True and self.sub_category.lower() in ['nonveg','non veg','non-veg']:
            raise ValidationError(f"{self.category.restaurant} cannot have Non-Vegetarian Items")

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
    price=models.IntegerField()
    description = models.TextField(null=True,blank=True)
    rating=models.CharField(max_length=50,choices=STATUS,null=True,default='Unrated')

    def __str__(self):
        return f"{self.itemname}({self.category.category}) from {self.restaurant}"
    
    class Meta:
        db_table='Menu'

