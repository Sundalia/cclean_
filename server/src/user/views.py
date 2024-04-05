from rest_framework import viewsets
from .models import *
from .serializers import *

# from django.contrib.auth import logout, authenticate
# from .utils import send_otp

class UserAPIView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
         
            
