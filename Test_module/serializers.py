from rest_framework import serializers

from Test_module.models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignment
        fields = '__all__'
        
        
    def validate(self,ins):
        if self.context['request'].user.roles.name == 'STUDENT':
            raise serializers.ValidationError('Users cannot create assignments!!!')
    
        super().validate(ins)