from rest_framework import viewsets, status
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from .utils import send_sms
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserAPIView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        data = request.data
        mobile = data.get('mobile', None)
        password = data.get('password', None)
        print(mobile, password)
        if mobile is None or password is None:
            return Response({'error': 'Введите номер телефона и пароль корректно'}, status = status.HTTP_400_BAD_REQUEST)
        user_exist = User.objects.get(mobile=mobile)
        print(user_exist)
        user = authenticate(username=mobile, password=password)
        print(user)
        if user is None:
            return Response({'error': 'Неверные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
           "id" : user.id,
           "username" : user.username,
           "last_name" : user.last_name,
           "mobile" : user.mobile,
           "email" : user.email,
           "password" : user.password,
           "is_cleaner" : user.is_cleaner,
           "is_customer" : user.is_customer,
           "is_active" : user.is_active,
           "is_verified": user.is_verified,
           "otp": user.otp
        }, status = status.HTTP_200_OK)





    """метод для ввода полученого пароля при успехе выдаётся новый токен"""
    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        instance = self.get_object()
        if (
            instance.is_verified == False
            and instance.otp == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() <= instance.otp_expiry
        ):
            instance.is_verified = True
            instance.is_active = True
            instance.otp_expiry = None
            instance.max_otp_try = os.getenv('MAX_OTP_TRY')
            instance.otp_max_out = None
            instance.save()

            token = RefreshToken.for_user(instance)
            token.payload.update({
                "user_id" : instance.id,
                "username" : instance.username
            })
            return Response({
                'refresh_token' : str(token), #refresh_token
                'access_token' : str(token.access_token)
            }, status=status.HTTP_201_CREATED)

            if (instance.otp != request.data.get("otp")) :
                return Response(
                    {"error":"Введён неправильный код"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            {"error":"Ошибка аккаунта, обратитесь в поддержку"},
            status=status.HTTP_400_BAD_REQUEST,
        )

        

        
    """метод для регенерации пароля и отправки его в смс"""    
    @action(detail=True, methods=['PATCH'])
    def regenerate_otp(self, request, pk=None):
        instance = self.get_object()
        print(instance)
        
        if int(instance.max_otp_try) == 0 and timezone.now() < instance.otp_max_out:
            return Response(
                'Максимальное количество попыток на пароль исчерпано, попробуйте снова через 10 минут',
                status=status.HTTP_400_BAD_REQUEST
            )
        otp=random.randint(1000,9999)
        otp_expiry=timezone.now() + timedelta(minutes=10)
        max_otp_try=int(instance.max_otp_try) - 1

        instance.otp=otp
        instance.otp_expiry=otp_expiry
        instance.max_otp_try = max_otp_try

        if max_otp_try == 0:
            instance.otp_max_out=timezone.now() + timedelta(minutes=10)
        elif max_otp_try == -1:
            instance.max_otp_try = os.getenv('MAX_OTP_TRY')
        else:
            instance.otp_max_out = None
            instance.max_otp_try = max_otp_try
        instance.save()
        send_sms(instance.mobile, otp)

        return Response({
            f"Новый пароль сгенерирован и отправлен на номер {instance.mobile}",
        }, status=status.HTTP_200_OK)
    

    """метод для выхода из аккаунта: убираем активность юзера и помещаем токен в черный список"""
    @action(detail=True, methods=['PATCH'])
    def logout(self, request, pk=None):
        refresh_token = request.data.get("refresh_token") # В запрос передать refresh_token
        user = self.get_object()
        user.is_verified = False
        user.save()
        if not refresh_token:
            return Response({'error': 'Необходим Refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist() # Добавить его в чёрный список

        except Exception as e:
            return Response({'error': 'Неверный Refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Вы успешно вышли из аккаунта'}, status=status.HTTP_200_OK)
        
        