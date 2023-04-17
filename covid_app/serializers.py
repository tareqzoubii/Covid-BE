from rest_framework import serializers
from .models import Covid

class CovidSerializer(serializers.ModelSerializer):
        class Meta:
          model= Covid
          fields='__all__'