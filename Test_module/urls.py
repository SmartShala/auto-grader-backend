from django.urls import path
from Test_module.views import (
    Basicview,
)

urlpatterns = (
    path('',Basicview.as_view()),
    # path('create/'),
    # path('start/')
)