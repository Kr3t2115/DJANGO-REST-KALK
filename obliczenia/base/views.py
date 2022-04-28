from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import obliczenie
from .serializers import obliczenieSer

@api_view(['GET'])
def ShowAll(request):
    products = obliczenie.objects.all()
    serializer = obliczenieSer(products, many=True)
    return Response(serializer.data)