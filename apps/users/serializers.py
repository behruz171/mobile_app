from rest_framework import serializers
from django.contrib.auth import get_user_model
import random
import string

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'birth_date')
    
    def create(self, validated_data):
        # Tasodifiy parol yaratish
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            birth_date=validated_data['birth_date'],
            password=password
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
