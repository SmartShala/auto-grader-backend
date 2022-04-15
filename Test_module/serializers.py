from rest_framework import serializers

from Test_module.models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignment
        fields = '__all__'