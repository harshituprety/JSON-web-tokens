from rest_framework import serializers
# import model from models.py
from .models import MovieModel,StudentModel

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ('id','title', 'description')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('id','name', 'email','city')