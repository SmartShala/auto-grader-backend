from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from Test_module.serializers import *
from Test_module.models import *
from rest_framework.renderers import JSONRenderer


# Create your views here.
class Basicview(APIView):
    def get(self,request,format=None):
        data = {
            'msg':'Hello World'
        }
        return Response(data)