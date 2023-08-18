from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()