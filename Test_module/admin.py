from django.contrib import admin
from Test_module.models import *
# Register your models here.
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Assignment)
admin.site.register(AssignmentAssigner)
admin.site.register(Questions)
admin.site.register(StudentAssignmentAns)
admin.site.register(StudentAnswers)