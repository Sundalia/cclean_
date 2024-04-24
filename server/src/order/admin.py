from django.contrib import admin
from .models import *

# admin.site.register(CleaningType)
# admin.site.register(CleaningTypeLocation)
# admin.site.register(CleaningTypeInclude)

# admin.site.register(CleaningTypeCanAdd)

admin.site.register(FurnitureCluttered)
admin.site.register(PollutionDegree)
admin.site.register(Promo)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(FeedBack)
admin.site.register(PortfolioImage)
admin.site.register(RoomType)



@admin.register(CleaningTypeCanAddList)
class CleaningTypeCanAddListAdmin(admin.ModelAdmin):
  list_display=(
    'name',
    'created',
    'updated'
  )
  list_filter=[
    'name'
  ]
  search_fields=[
    'name'
  ]
  show_change_link=True
  view_on_site=False

"""Можно добавить включая списки""" 
@admin.register(CleaningTypeCanAdd)
class CleaningTypeCanAddAdmin(admin.ModelAdmin):
  fields=['name', 'price', 'can_add_list']
  ordering=['name']
  filter_horizontal=['can_add_list']
  list_display=[
    'name',
    'created',
    'updated'
  ]
  list_filter=[
    'name'
  ]
  search_fields=[
    'name'
  ]
  extra=0
  show_change_link=True
  view_on_site=False



"""Список что входит"""
@admin.register(CleaningTypeIncludeList)
class CleaningTypeIncludeListAdmin(admin.ModelAdmin):
  list_display=(
    'name',
    'created',
    'updated'
  )
  list_display=[
    'name',
    'created',
    'updated'
  ]
  list_filter=[
    'name'
  ]
  search_fields=[
    'name'
  ]
  show_change_link=True
  view_on_site=False

"""Категория что входит включая список"""
@admin.register(CleaningTypeInclude)
class CleaningTypeIncludeAdmin(admin.ModelAdmin):
  fields=['name', 'include_list']
  filter_horizontal=['include_list']
  list_display=[
    'name',
    'created',
    'updated'
  ]
  list_filter=[
    'name',
    'created',
    'updated'
  ]
  search_fields=[
    'name',
    'created',
    'updated'
  ]
  extra=0
  show_change_link=True
  view_on_site=False
    
  
"""Локации включая что входит и можно добавить"""
# class CanAddInline(admin.StackedInline):
#   model=CleaningTypeCanAdd
#   extra=0
#   show_change_link=True
#   view_on_site=False

# class IncludeInline(admin.StackedInline):
#   model=CleaningTypeInclude
#   extra=0
#   show_change_link=True
#   view_on_site=False

@admin.register(CleaningTypeLocation)
class CleaningTypeLocationAdmin(admin.ModelAdmin):
  fields=(
    'cleaning_type',
    'name',
    'subname',
    'include',
    'can_add'
  )
  list_display=(
    'name',
    'subname',
    'cleaning_type',
  )
  
  
"""Типы уборки включая локации и изображения портфолио"""
class LocationInline(admin.TabularInline):
  model=CleaningTypeLocation
  fields=(
    'name',
    'include',
    'can_add'
  )
  filter_vertical=['include', 'can_add']
  extra=0
  show_change_link=True
  view_on_site=False
  
class PortfolioInline(admin.TabularInline):
  model=PortfolioImage
  fields=(
    'name',
    'picture',
    'description'
  )
  extra=0
  show_change_link=True
  view_on_site=False

@admin.register(CleaningType)
class CleaningTypeAdmin(admin.ModelAdmin):
  inlines=[LocationInline, PortfolioInline]
  list_display=(
    'name',
    'description',
    'subdescription',
    'price'
  )
  view_on_site=False
  # site_url= """Добавить адреса для кнопки СМОТРЕТЬ НА САЙТЕ"""