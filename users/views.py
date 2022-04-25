from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from users.serializers import *
from users.models import *
from rest_framework.renderers import JSONRenderer
# Create your views here.

class helloworld(APIView):
    
    def get(self,request,format=None):
        data = {
            'msg':'Hello World'
        }
        return Response(data)
    

class GetStudentsByFilter(generics.ListAPIView):
    
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = StudentBodySerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['name','student_id','roll_no']
    rendered_classes = [JSONRenderer]
    
    def get_queryset(self):
        try:
            return Student.objects.all().order_by('-id')
        except Student.DoesNotExist:
            return Http404
