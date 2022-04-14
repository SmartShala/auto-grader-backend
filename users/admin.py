from django.contrib import admin
from users.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Syllabus)
admin.site.register(Semester)
admin.site.register(Branch)
