from django.urls import path
from users.views import *
urlpatterns = [
    path('',helloworld.as_view()),
    path('students/',GetStudentsByFilter.as_view()),
]