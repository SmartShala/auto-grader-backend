from rest_framework import serializers
from users.models import *



class StudentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','student_id','roll_no','academic_year','semester')