from django.db import models

# Create your models here.
#Convert tables into python object to ineract with db table 
class property(models.Model):
    title = models.CharField(max_length=150) #means data is string
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=150)
    #image
    
    def __str__(self):
        return self.title
