from django.urls import path
from Test_module.views import (
    AssignmentView,AssignmentDetailView
)

urlpatterns = (
    path('',AssignmentView.as_view()),
    path('<pk>/',AssignmentDetailView.as_view()),
    # path('start/')
)