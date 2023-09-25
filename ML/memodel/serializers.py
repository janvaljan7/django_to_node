from rest_framework import serializers 
from . import models

class interestSerializer(serializers.ModelSerializer):
    """Serializing the date form"""
    class Meta: 
        model = models.interest
        fields = ['id', 'first', 'second', 'third' ]

    