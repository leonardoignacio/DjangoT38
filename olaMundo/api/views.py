from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def apiOla(request):
    return Response("Olá Mundo!!!!!")

