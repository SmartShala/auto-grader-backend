from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import status,permissions,filters
from rest_framework import generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from Test_module.serializers import *
from Test_module.models import *
from rest_framework.renderers import JSONRenderer
from auto_grader.paginators import CustomPagination


# Create your views here.
class AssignmentView(generics.ListCreateAPIView):
    """Use Assignment view to get assignments for one user
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignmentSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter)
    pagination_class = CustomPagination
    ordering_fields = ('-submit_by','-created_at','total_marks','submissions')
    ordering = ('-submit_by')
    rendered_classes = (JSONRenderer)

    def get_queryset(self):
        user = self.request.user
        if user.roles.name == 'TEACHER':
            return Assignment.objects.filter(assigned_by_user=user)
        
        elif user.roles.name == 'STUDENT':
            try:
                student = Student.objects.get(user=user)    
                as_mappers = AssignmentAssigner.objects.select_related(
                    'assignment').filter(
                        Q(student=student) |
                        Q(section=student.section) |
                        Q(semester=student.section.semester) |
                        Q(branch=student.section.branch) 
                    ).values(assignment)
                return Assignment.objects.filter(assignmentassigner__in=as_mappers)
            except:
                return Http404
        elif user.roles.name == 'ADMIN' or user.roles.name == 'SUPERADMIN':
            return Assignment.objects.all()
    
