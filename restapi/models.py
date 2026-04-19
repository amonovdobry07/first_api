from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Cars(models.Model): 
    owner = models.ForeignKey(User, related_name="cars", on_delete=models.CASCADE, null=True)
    img = models.ImageField()
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    