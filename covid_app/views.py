from django.shortcuts import render
from .models import Covid
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import CovidSerializer
from rest_framework.response import Response
import requests
# Create your views here.

class CovidListCreateView(ListCreateAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer

class CovidDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer

class allCountries(APIView):
    serializer_class = CovidSerializer

    def get(self,request):
        url='https://api.covid19api.com/summary'
        req = requests.get(url).json()
        return Response(req)
    
class CountryCases(APIView):
        def get(self,request,format=None):
            Country=request.GET['Country']
            f=request.GET["from"]
            to=request.GET['to']
            url=f'https://api.covid19api.com/country/{Country}/status/confirmed?from={f}&to={to}'
            r = requests.get(url).json()
            return Response(r)