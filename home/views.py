from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST','PUT'])
def home(request):
    return Response({'name':'zara'})