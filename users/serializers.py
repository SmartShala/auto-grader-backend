from rest_framework import serializers
from users.models import *



class StudentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id','name','section','student_id','roll_no','academic_year','semester')