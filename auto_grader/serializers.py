from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.models import TokenUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
    
class CustomTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if self.user.last_login == None:
            data['is_new'] = True
        else:
            data['is_new'] = False

        data['user'] = self.user.roles.name
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
    

class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer
