from django.urls import path
from Test_module.views import (
    AssignmentView,
)

urlpatterns = (
    path('',AssignmentView.as_view()),
    # path('create/'),
    # path('start/')
)