from rest_framework import serializers
from .models import *
import os
import django.utils.timezone
from datetime import timedelta
import random
from .utils import send_sms
from django.contrib.auth.models import Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=(
            'id',
            'username', 
            'last_name', 
            'mobile', 
            'email',  
            'password',
            'is_cleaner',
            'is_customer',
            'is_active',
            'is_verified',
            'groups',
            'otp',
            'otp_expiry',
        )
        
    def create(self, data):
        otp=random.randint(1000,9999)
        otp_expiry=django.utils.timezone.now() + timedelta(minutes=10)
        
        user = User(
            mobile=data["mobile"],
            username=data["username"],
            is_cleaner=data["is_cleaner"],
            is_customer=data["is_customer"],
            otp=otp,
            otp_expiry=otp_expiry,
            max_otp_try=os.getenv("MAX_OTP_TRY"),
            is_active=False,
            is_verified=False

        )
        user.set_password(data["password"])
        user.save()
        if (
            user.is_customer == True
            and user.is_cleaner  == False
        ):
            user.groups.add(Group.objects.get(name='customer'))
        else:
            user.groups.add(Group.objects.get(name='cleaner'))

        send_sms(data["mobile"], otp)
        return user
        
        
        
        
class TokenSerializer(TokenObtainPairSerializer):
    class Meta:
        serializers = TokenObtainPairSerializer
        fields = '__all__'
