from rest_framework import serializers
from core.models import Movie, User_Movie
from core import models

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for movie object"""

    class Meta:
        model = Movie
        fields = '__all__'

class User_MovieSerializer(serializers.ModelSerializer):
    """Serializer for a user_movie table"""
    
    class Meta:
        model = User_Movie
        fields = '__all__'
        read_only_fields = ('insert_date', )

    

