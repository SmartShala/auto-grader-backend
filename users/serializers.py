from rest_framework import serializers
from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')

class StudentBodySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    section = serializers.CharField(source='section.name')
    academic_year = serializers.DateField(source='section.semester.Academic_Year')
    branch = serializers.CharField(source='section.branch.name')
    semester = serializers.IntegerField(source='section.semester.semester_number')
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id','name',
                  'section','semester',
                  'academic_year','branch',
                  'student_id','email','roll_no',
                  'profile_image')