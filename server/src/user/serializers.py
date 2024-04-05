from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'id',
            'is_staff',
            'username', 
            'last_name', 
            'mobile', 
            'email',  
            'password',
            'is_cleaner',
            'is_customer'
        )
        
        