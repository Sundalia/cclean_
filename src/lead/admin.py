from django.contrib import admin
from .models import *

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
  list_display=(
    'cleaning_type',
    'counter_room',
    'counter_toilet',
    'phone_number',
    'created',
    'updated'
  )
  list_filter=[
    'cleaning_type',
    'created',
    'updated'
  ]
