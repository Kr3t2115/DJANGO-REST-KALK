from rest_framework import serializers

from .models import obliczenie

class obliczenieSer(serializers.ModelSerializer):
    class Meta:
        model = obliczenie
        fields = '__all__'