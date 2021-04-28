from django.db import models
from django.core.exceptions import ValidationError

from restaurant.models import Restaurant
from accounts.models import User
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

    def category_name(self):
        return self.category.category

def location(instance,filename):
    return f"{instance.restaurant.city}/{instance.restaurant.name}/menu/{filename}"

class Menu(models.Model):
    
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category=models.ForeignKey(Sub_Category, on_delete=models.CASCADE,related_name='menu')
    itemname=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to=location)
    rating_average = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    available= models.BooleanField(default=True)

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

    @property
    def rating_average(self):
        return  (0 if self.ratings.aggregate(models.Avg('rating')).get('rating__avg') is None else self.ratings.aggregate(models.Avg('rating')).get('rating__avg'))
    
    @property
    def review_count(self):
        return self.ratings.count()

class Rating(models.Model):
    STATUS = (
        (0,('Unrated')),
       (1, ('Bad')),
       (2,('Satisfactory')),
       (3, ('Good')),
       (4, ('Excellent')),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='ratings')
    rating=models.PositiveIntegerField(choices=STATUS,null=True,default='Unrated')


    class Meta:
        unique_together = ['user', 'item']

    def __str__(self):
        return f"{self.user} rated {self.item} as {self.rating}"
    
    def item_name(self):
        return self.item.itemname
    
