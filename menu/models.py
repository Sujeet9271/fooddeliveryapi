from django.db import models
from restaurant.models import Restaurant

# Create your models here.
class Category(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='category',default=1)
    category=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category} ({self.restaurant})"

    class Meta:
        db_table='Category'


class Sub_Category(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='sub_category',default=1)
    sub_category=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sub_category}({self.category} from {self.category.restaurant})"
    
    class Meta:
        db_table='Sub_Category'


class Menu(models.Model):
    STATUS = (
        ('Unrated',('Unrated')),
       ('Bad', ('Bad')),
       ('Satisfactory',('Satisfactory')),
       ('Good', ('Good')),
       ('Excellent', ('Excellent')),
    )
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE,default=1)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    sub_category=models.ForeignKey(Sub_Category, on_delete=models.CASCADE,related_name='menu',default=1)
    itemname=models.CharField(max_length=255)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    rating=models.CharField(max_length=50,choices=STATUS,null=True,default='Unrated')

    def __str__(self):
        return f"{self.itemname}({self.category.category}) from {self.restaurant}"
    
    class Meta:
        db_table='Menu'

