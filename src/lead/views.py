from rest_framework import viewsets
from .models import *
from .serializers import *

class LeadAPIView(viewsets.ModelViewSet):
  queryset=Lead.objects.all()
  serializer_class=LeadSerializer