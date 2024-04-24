from rest_framework import serializers
from .models import *




class RoomTypeSerializer(serializers.ModelSerializer):
    model=RoomType
    fields=(
        'name',
        'type',
        'created',
        'updated',
        'is_published'
    )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=(
            'customer', 
            'cleaning_type', 
            'square', 
            'furniture_cluttered', 
            'pollution_degree',
            'room_type',
            'cleaning_date',
            'cleaning_time',
            'photo',
            'window_clean',
            'address',
            'comment',
            'promo',
            'price',
            'created',
            'updated',
            'is_published',
            'cleaners_photo'
        )
        
        
class FurnitureClutteredSerialier(serializers.ModelSerializer):
    class Meta:
        model=FurnitureCluttered
        fields=(
            'name',
            'description',
            'created',
            'updated',
            'is_published'
        )
        

class PollutionDegreeSerialier(serializers.ModelSerializer):
    class Meta:
        model=PollutionDegree
        fields=(
            'name',
            'description',
            'created',
            'updated',
            'is_published'
        )
        
class  PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promo
        fields=(
            'name',
            'description',
            'price',
            'promocode',
            'cleaning_type',       
            'created',
            'updated',
            'is_published'
        )
        
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderStatus
        fields=(
            'order',
            'is_confirmed',
            'is_started',
            'is_finished',
            'is_paid'
        )
        
class CleaningTypeIncludeSerializer(serializers.ModelSerializer):
    
    include_list=serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )
    
    
    class Meta:
        model=CleaningTypeInclude
        fields=(
            'name',
            'include_list'
        )
        
class CleaningTypeIncludeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CleaningTypeIncludeList
        fields=(
            'cleaning_type_include',
            'name'
        )
        
class CleaningTypeCanAddSerializer(serializers.ModelSerializer):
    
    can_add_list=serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )    

    class Meta:
        model=CleaningTypeCanAdd
        fields=(
            'name',
            'price',
            'can_add_list'
        )
        
class CleaningTypeCanAddListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CleaningTypeCanAddList
        fields=(
            'can_add',
            'name'
        )
        
        
        
class CleaningTypeLocationSerializer(serializers.ModelSerializer):
    include=CleaningTypeIncludeSerializer(
        many=True
    )
    
    can_add=CleaningTypeCanAddSerializer(
        many=True
    ) 
    
    class Meta:
        model=CleaningTypeLocation
        fields=(
            'cleaning_type',
            'name',
            'subname',
            'include',
            'can_add'
        )
        
        
class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioImage
        fields=(
            'cleaning_type',
            'name',
            'picture',
            'description',
            'created',
            'updated',
            'is_published'
        )
        
        
        
class  CleaninigTypeSerializer(serializers.ModelSerializer):
    location=CleaningTypeLocationSerializer(
        many=True
    )
    portfolio=PortfolioImageSerializer(
        many=True
    )
    
    class Meta:
        model=CleaningType
        fields=(
            'name',
            'description',
            'subdescription',
            'location',
            'price',
            'portfolio'
    )
        
        
class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields=(
            'name',
            'order',
            'feedback_body',
            'feedback_rating',
            'created',
            'updated',
            'is_published'
        )