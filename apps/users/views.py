from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from .utils import send_verification_email

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Tasdiqlash PIN kodini yaratish
        # verification = EmailVerification.objects.create(user=user)
        
        
        # Email yuborish
        # send_verification_email(user.email, verification.pin_code)

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)


class VerifyEmailView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        pin_code = request.data.get('pin_code')

        try:
            verification = EmailVerification.objects.get(user__email=email, pin_code=pin_code)
            # PIN kodni tasdiqlash va foydalanuvchini faollashtirish
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
            return Response({'status': 'verified'})
        except EmailVerification.DoesNotExist:
            return Response({'error': 'Invalid or expired PIN code'}, status=400)



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        first_name = serializer.validated_data['first_name']

        try:
            user = User.objects.get(email=email, first_name=first_name)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # JWT token yaratish
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_200_OK)