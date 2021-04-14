from django.db import models
from city.models import City
# Create your models here.

def location(instance,filename):
    return f"{instance.city.name}/{instance.name}/Restaurant/{filename}"

class Restaurant(models.Model):
    Rating = (
        ('Unrated',('Unrated')),
       ('Bad', ('Bad')),
       ('Satissfactory',('Satisfactory')),
       ('Good', ('Good')),
       ('Excellent', ('Excellent')),
   )
    Status=(
        ('Open',('Open')),('Closed',('Closed'))
    )
    city=models.ForeignKey(City,on_delete=models.CASCADE, related_name='restaurant')
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phnumber=models.IntegerField(unique=True)
    status=models.CharField(max_length=50,choices=Status,default='Open')
    rating=models.CharField(max_length=50,choices=Rating,default='Unrated',null=True)
    veg_only = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True,upload_to=location)
    



    def __str__(self):
        return f"{self.name}-{self.city}"

    class Meta:
        db_table = 'Restaurant'

    def city_name(self):
        return self.city.name