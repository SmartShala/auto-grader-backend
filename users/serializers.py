from rest_framework import serializers
from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')

class StudentBodySerializer(serializers.ModelSerializer):
    email = serializers.IntegerField(source="user.email")
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('id','name','section','student_id','email','roll_no','semester')