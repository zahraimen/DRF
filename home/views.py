from django.shortcuts import render
# from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Home(APIView):
    def get(self,request):
        name=request.query_params['name']
        return Response({'name':name})
    # def post(self,request):
    #     name=request.data['name']
    #     return Response({'name':name})
    