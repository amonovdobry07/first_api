from rest_framework import serializers
from .models import Cars

class CarsSeriaLizer(serializers.ModelSerializer): 
    class Meta: 
        model =  Cars
        fields = "__all__"


