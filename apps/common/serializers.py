from rest_framework import serializers
from .models import *




class SponsorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        exclude = ('status', 'payment_type')

    
    def validate(self, attrs):
        company_name = attrs.get('company_name')
        user_type = attrs.get('user_type')


        return super().validate(attrs)
    

class StudentSponsorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSponser
        fields = "__all__"

    
    def validate(self, attrs):
        from django.db.models import Sum
        student = attrs['student'] # Toshmat
        sponsor = attrs['sponsor'] # Eshmat
        amount = attrs['amount'] # 1 000 000 
        sarflangan_summa = sponsor.student_amounts.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        sponsor_current_amount = sponsor.wallet - sarflangan_summa
        if amount > sponsor_current_amount:
            raise serializers.ValidationError(
                detail={'msg': f"Sponsorda xozir mavjud bo'lgan summa {sponsor_current_amount}"}
            )
        
        student_current_amount = student.sponsor_amounts.all().aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        if  student.contract - student_current_amount < amount:
            raise serializers.ValidationError(
                detail={'msg': f"Studentda qolgan kontrakt miqdori {student.contract - student_current_amount}"}
            )

        return super().validate(attrs)


class StudentListSerializer(serializers.ModelSerializer):
    allocated_amount = serializers.SerializerMethodField()
    university = serializers.CharField(source='university.name')

    def get_allocated_amount(self,obj):
        from django.db.models import Sum  
        return obj.sponsor_amounts.aggregate(total=Sum('amount'))['total'] or 0
    
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'university', 'contract', 'degree', 'allocated_amount')

    # def to_representation(self, instance):
    #     from django.db.models import Sum    
    #     data = super().to_representation(instance)
    #     data['allocated_amount'] = instance.sponsor_amounts.aggregate(total=Sum('amount'))['total'] or 0
    #     return data
    
