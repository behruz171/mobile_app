from .serializers import SponsorCreateSerializer, StudentSponsorCreateSerializer,StudentListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from . import models
from rest_framework.views import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.db.models import Sum


class SponsorCreateAPIView(CreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer



class StudentSponsorCreateAPIView(CreateAPIView):
    queryset = models.StudentSponser.objects.all()
    serializer_class = StudentSponsorCreateSerializer 
    

class StudentListAPIView(ListAPIView):
    queryset = models.Student.objects.all()    
    serializer_class = StudentListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['university', 'degree']
    search_fields = ('full_name',)


class TotalAmountStatisticAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        total_required_amount = models.Student.objects.aggregate(total=Sum('contract'))['total']
        total_paid_amount = models.StudentSponser.objects.aggregate(total=Sum('amount'))['total']
        return Response(
            data={
                'total_required_amount': total_required_amount,
                'total_paid_amount': total_paid_amount,
                'total_remain_amount': total_required_amount - total_paid_amount
            }
        )
    

class MonthlyStatisticAPIView(APIView):

    def get(self, request, *args, **kwargs):
        from datetime import date
        this_year = date.today().year

        results = []
        for i in range(1, 13):
            results.append({
                'month': self.get_month(i),
                'students':  models.Student.objects.filter(created_at__month=i, created_at__year=this_year).count(),
                'sponsors': models.Sponsor.objects.filter(created_at__month=i, created_at__year=this_year).count()
            })

        return Response(results)

    
    def get_month(self, month_in_number):
        l = {
            1: 'Yanvar',
            2: 'Fevral', 
            3: 'Mart',
            4: 'Aprel',
            5: 'May',
            6: 'Iyun',
            7:'Iyul',
            8: 'Avgust',
            9: 'Sentyabr',
            10: 'Oktyabr',
            11: 'Noyabr',
            12: 'Dekabr'
        }
        return l[month_in_number]
    
