from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import viewsets
from . import models
from rest_framework.views import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.db.models import Sum
from .serializers import *
from .permission import *

# class CreateContentView(CreateAPIView):
#     queryset = Content.objects.all()
#     serializer_class = CreateContentSerializer
#     permission_classes = [IsSuperUser, IsAuthenticated]


# class CreateCategoryView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CreateCategorySerializer
#     permission_classes = [IsSuperUser, IsAuthenticated]


# class ContentListView(ListAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer

# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class QuestionsListView(ListAPIView):
#     queryset = Questions.objects.all()
#     serializer_class = QuestionsListSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class HomePageView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = HomePageSerializer