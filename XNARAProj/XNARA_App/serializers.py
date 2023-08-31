from rest_framework import serializers
from .models import  CustomerData

class CustomerDataSerializer(serializers.ModelSerializer):
    '''This is serializer class to serialize object and convert into python datastructure and
    python datastructure to complex objects '''
    class Meta:
        model=CustomerData
        fields='__all__'
