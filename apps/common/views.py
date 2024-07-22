from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView
from . import models
from rest_framework.views import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.db.models import Sum
from .serializers import *
from .permission import *

class CreateContentView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = CreateContentSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]


class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = [IsSuperUser, IsAuthenticated]


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer