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
    rendered_classes = (JSONRenderer,)

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
                    )
                return Assignment.objects.filter(assignmentassigner__in=as_mappers)
            except:
                raise Http404
        elif user.roles.name == 'ADMIN' or user.roles.name == 'SUPERADMIN':
            return Assignment.objects.all()
    
class AssignmentDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignmentDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    rendered_classes = (JSONRenderer,)
    
    def get_object(self,pk):
        try:
            return Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        assignment = self.get_object(pk)
        if request.user.roles.name == 'STUDENT':
            try:
                student = Student.objects.get(user=request.user)
            except Student.DoesNotExist:
                student = None
            # Part of this code tries to check if student has proper access to the Assignment or not
            checker = AssignmentAssigner.objects.filter(
                Q(assignment = assignment) &
                Q(student = student) |
                Q(section = student.section) |
                Q(semester = student.section.semester) |
                Q(semester = student.section.branch)
            )
            if not checker.exists():
                return Response({
                    'error':'No Such Assignment Found!'
                },400)
        another_obj = StudentAssignmentAns.objects.filter(
                assignment=assignment,
                student=student
            ) if student else None
        
        if another_obj is not None and another_obj.exists():
            serializer = StudentAssDetailSerializer(another_obj[0])
        else:
            serializer = self.serializer_class(object)
        data = serializer.data
        data['user'] = request.user.roles.name
        return Response(data)

