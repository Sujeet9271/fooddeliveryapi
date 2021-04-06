from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    pincode=models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table='City'