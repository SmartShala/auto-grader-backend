from rest_framework import serializers

from Test_module.models import Assignment, AssignmentAssigner, AssignmentQuestion, Question
from users.models import Teacher

class AssignmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Assignment
        fields = '__all__'
        
        
    def validate(self,ins):
        request = self.context['request']
        if request.user.roles.name == 'STUDENT':
            raise serializers.ValidationError('Users cannot create assignments!!!')
        try:
            ins['assigned_by'] = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            raise serializers.ValidationError('Only teachers can create assignments!!!')
        
        super().validate(ins)
        
class QuestionSerializer(serializers.Serializer):
    
    class Meta:
        model = AssignmentQuestion
        depth = 1
        fields = ('marks','question')
        

class AssignmentDetailSerializer(serializers.ModelSerializer):
    
    questions = QuestionSerializer(source='assignmentquestion_set',many=True)
    class Meta:
        model = Assignment
        fiels = (
            'id','name','questions',
            'subject','topic','created_at',
            'updated_at','total_marks',
            'submissions',
            )
        
class StudentAssDetailSerializer(serializers.ModelSerializer):

    assignment = AssignmentDetailSerializer()
    class Meta:
        model = AssignmentAssigner
        fields = (
            'id','assignment',
            'is_submitted','submit_time',
            'score'
            )
        
        def to_representation(self,ins):
            data = super().to_representation(ins)
            data = {
                **data.pop('assignment'),
                **data
            }
            return data
