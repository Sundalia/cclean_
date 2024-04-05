from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username=models.CharField(max_length=150, verbose_name='Имя', unique=False)
    mobile=models.CharField(max_length=12, verbose_name='Номер телефона', unique=True)
    email=models.CharField(max_length=120, verbose_name='Почта', blank=True, null=True)
    is_cleaner=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
    
    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=['username', 'password', 'is_cleaner', 'is_customer']
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
        unique_together=('mobile', 'password')
    
    @property
    def is_authenticated(self):
        return True
    
    def __str__(self):
        return self.username