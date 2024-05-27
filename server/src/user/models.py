from django.db import models
from django.contrib.auth.models import (AbstractUser , PermissionsMixin, UserManager)
import os
from rest_framework.authtoken.models import Token




class CustomUserManager(UserManager):
    def create_user(self, mobile, password=None):
        if not mobile:
            raise ValueError('Номер телефона обязателен')            
        user=self.model(mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile, password):
        user=self.create_user(mobile, password)
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    
    
class User(AbstractUser, PermissionsMixin):
    username=models.CharField(max_length=150, verbose_name='Имя', unique=False)
    mobile=models.CharField(max_length=12, verbose_name='Номер телефона', unique=True)
    email=models.CharField(max_length=120, verbose_name='Почта', blank=True, null=True)
    is_cleaner=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    otp=models.CharField(max_length=6, verbose_name='OTP-пароль', blank=True, null=True)
    otp_expiry=models.DateTimeField(blank=True, null=True, verbose_name='дата и время пароля отп')
    max_otp_try=models.CharField(max_length=2, default=os.getenv('MAX_OTP_TRY'))
    otp_max_out=models.DateTimeField(blank=True, null=True)
    registred_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    
    
    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=['username', 'password', 'is_cleaner', 'is_customer']
    
    objects=CustomUserManager()

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        unique_together=('mobile', 'password')
    
    def __str__(self):
        return self.username



    