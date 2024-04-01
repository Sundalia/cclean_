from rest_framework import serializers
from .models import *

class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model=Lead
    fields=(
      'cleaning_type',
      'counter_room',
      'counter_toilet',
      'phone_number'
    )
    
    