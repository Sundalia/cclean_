from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LeadAPIView

router=DefaultRouter()
router.register(r'leads', LeadAPIView)
urlpatterns = [
    path('', include(router.urls))
]
