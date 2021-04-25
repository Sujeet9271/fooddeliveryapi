from django.db import models

# Create your models here.
def location(instance,filename):
    return f"{instance.name}/{filename}"

class City(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to=location)
    pincode=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table='City'