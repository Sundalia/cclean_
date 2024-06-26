from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserAPIView

router=DefaultRouter()
router.register(r'users',UserAPIView)
urlpatterns = [
    path('', include(router.urls))
]