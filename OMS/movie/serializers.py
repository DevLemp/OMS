from rest_framework import serializers
from core.models import Movie, User_Movie
from django.utils import timezone
from core import models

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for movie object"""

    class Meta:
        model = Movie
        fields = '__all__'

class User_MovieSerializer(serializers.ModelSerializer):
    """Serializer for a user_movie table"""
    price = serializers.SerializerMethodField('rental_price')
    
    def rental_price(self, obj):
        now = timezone.now()
        price = obj.price
        if (now-obj.insert_date).days == 0:
            pass
        elif (now-obj.insert_date).days <= 3:
            price = (now-obj.insert_date).days
        else:
            price = 3 + 0.5*((now-obj.insert_date).days - 3)
        return price

    class Meta:
        model = User_Movie
        fields = '__all__'

