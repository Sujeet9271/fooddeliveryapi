from django.db import models
from city.models import City
from accounts.models import User
# Create your models here.

def location(instance,filename):
    return f"{instance.city.name}/{instance.name}/Restaurant/{filename}"

class Restaurant(models.Model):
    
    Status=(
        ('Open',('Open')),('Closed',('Closed'))
    )
    city=models.ForeignKey(City,on_delete=models.CASCADE, related_name='restaurant')
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phnumber=models.CharField(max_length=10,unique=True)
    status=models.CharField(max_length=50,choices=Status,default='Open')
    veg_only = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True,upload_to=location)
    rating_average = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)

    # def update_review_fields(self):
    #     ratings = self.ratings.all()
    #     self.rating_average = ratings.aggregate(models.Avg('rating')).get('rating__avg')
    #     self.review_count = ratings.count()
    #     self.save(update_fields=['rating_average', 'review_count'])
    



    def __str__(self):
        return f"{self.name}-{self.city}"

    class Meta:
        db_table = 'Restaurant'

    def city_name(self):
        return self.city.name
    
    @property
    def rating_average(self):
        return  (0 if self.ratings.aggregate(models.Avg('rating')).get('rating__avg') is None else self.ratings.aggregate(models.Avg('rating')).get('rating__avg'))
    
    @property
    def review_count(self):
        return self.ratings.count()
    
    


class RestaurantRating(models.Model):
    Rating = (
        (0,('Unrated')),
       (1, ('Bad')),
       (2,('Satisfactory')),
       (3, ('Good')),
       (4, ('Excellent')),
   )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    rating=models.PositiveIntegerField(choices=Rating,default='Unrated',null=True)

    class Meta:
        unique_together = ['user', 'restaurant']

    def __str__(self):
        return f"{self.user} rated {self.restaurant} as {self.rating}"

    def restaurant_name(self):
        return self.restaurant.name

