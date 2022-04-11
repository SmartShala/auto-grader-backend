from rest_framework import serializers
from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('contact', 'id')

class StudentBodySerializer(serializers.ModelSerializer):
    contact = serializers.IntegerField(source="user.contact")
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id','name','section','student_id','roll_no','academic_year','semester')