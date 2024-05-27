from rest_framework import viewsets, permissions, status
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.serializers import serialize
import json

class OrderAPIView(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes = [

    ]
    @action(detail=False, methods=['PATCH'])
    def get_users_orders(self, request):
        data = request.data
        customer = data.get("customer",  None)

        if customer is None:
            return Response({'error': 'Вы не авторизованы, Вы каак сюда попали?'}, status = status.HTTP_400_BAD_REQUEST)
        orders = Order.objects.get(customer=customer)
        serialized_orders = serialize('json',[orders])
        serialized_orders = json.loads(serialized_orders)


        return JsonResponse(serialized_orders, safe=False, status=200)


class CleaningTypeAPIView(viewsets.ModelViewSet):
    queryset=CleaningType.objects.all()
    serializer_class=CleaninigTypeSerializer
    permission_classes=[
        
    ]
    
class CleqaningTypeLocationAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeLocation.objects.all()
    serializer_class=CleaningTypeLocationSerializer
    
class CleaningTypeIncludeAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeInclude.objects.all()
    serializer_class=CleaningTypeIncludeSerializer
    
class CleaningTypeIncludeListAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeIncludeList.objects.all()
    serializer_class=CleaningTypeIncludeListSerializer
    
class CleaningTypeCanAddAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeCanAdd.objects.all()
    serializer_class=CleaningTypeCanAddSerializer
    
class CleaningTypeCanAddListAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeCanAddList.objects.all()
    serializer_class=CleaningTypeCanAddListSerializer
    
class FurnitureClutteredAPIView(viewsets.ModelViewSet):
    queryset=FurnitureCluttered.objects.all()
    serializer_class=FurnitureClutteredSerialier
    
class PollutionDegreeAPIView(viewsets.ModelViewSet):
    queryset=PollutionDegree.objects.all()
    serializer_class=PollutionDegreeSerialier
    
class PromoAPIView(viewsets.ModelViewSet):
    queryset=Promo.objects.all()
    serializer_class=PromoSerializer
    permission_classes = [

    ]
    
class OrderStatusAPIView(viewsets.ModelViewSet):
    queryset=OrderStatus.objects.all()
    serializer_class=OrderStatusSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
class PortfolioImageAPIView(viewsets.ModelViewSet):
    queryset=PortfolioImage.objects.all()
    serializer_class=PortfolioImageSerializer
    # permission_classes=[
    #     permissions.IsAuthenticated
    # ]
    
class FeedbackAPIView(viewsets.ModelViewSet):
    queryset=FeedBack.objects.all()
    serializer_class=FeedBackSerializer
    
    
class RoomTypeAPIView(viewsets.ModelViewSet):
    queryset=RoomType.objects.all()
    serializer_class=RoomTypeSerializer