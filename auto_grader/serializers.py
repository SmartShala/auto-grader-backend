from rest_framework.views import Response
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.models import TokenUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from users.models import User  
    

class CustomTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):        
        data = super().validate(attrs)
        data['error'] = False
        data['user'] = self.user.roles.name
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
    

class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenSerializer

    
    
    def post(self, request, *args, **kwargs):
        data = request.data

        # Running Custom Validation for OTP Validation and User Validation.
        if 'email' not in data:
            return Response(data={
                'error':True,
                "msg":"Invalid Email Address"
            },status=400)
        try:
            sent_user = User.objects.get(id=data['email'])
        except User.DoesNotExist:
            return Response(data={
                'error':True,
                "msg":'User Does not Exist. Please Contact Administrator.'
            },status=400)
        
        is_new:bool = sent_user.last_login is not None
        otp:bool = is_new or sent_user.twoFactor
            
        if 'password' not in data:
            if otp:
                "Add OTP SENDER HERE"
                ...
            return Response(data={
                'is_new': is_new ,
                'otp': otp,
                "error":False,
                "msg":None
            })
        
        else:
            # IF OTP IS VALIDATED
            if otp:
                if 'otp' not in data:
                    return Response(data={
                        "error":True,
                        "msg":"No OTP Provided"
                    })
                "Do otp Validation Here"
                ...
            # If Password is to be set
            if is_new:
                sent_user.set_password(data['password'])
                sent_user.save()
            
    
            super().post(request,*args,**kwargs)
