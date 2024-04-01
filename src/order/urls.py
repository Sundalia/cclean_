from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r'orders',OrderAPIView)
router.register(r'cleaning_type', CleaningTypeAPIView)
router.register(r'cleaning_type_location', CleqaningTypeLocationAPIView)
router.register(r'cleaning_type_include', CleaningTypeIncludeAPIView)
router.register(r'cleaning_type_include_list', CleaningTypeIncludeListAPIView)
router.register(r'cleaning_type_can_add', CleaningTypeCanAddAPIView)
router.register(r'cleaning_type_include_list', CleaningTypeCanAddListAPIView)
router.register(r'furniture_cluttered', FurnitureClutteredAPIView)
router.register(r'thing_cluttered', ThingsClutteredAPIView)
router.register(r'pollution_degree', PollutionDegreeAPIView)
router.register(r'promo', PromoAPIView)
router.register(r'order_status', OrderStatusAPIView)


urlpatterns = [
    
    path('', include(router.urls))
]
