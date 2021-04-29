from django.shortcuts import render
from .models import Data
from data.serializers import DataSerializer
from rest_framework import viewsets


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer



def home(request):
    context ={
            'datas': Data.objects.all()
              }
    return render(request,'data/home.html',context)




  