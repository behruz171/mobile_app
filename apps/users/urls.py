from django.urls import path, include
from .views import *
from apps.common.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    

    path('', include(router.urls)),
    path('home-page/', HomePageView.as_view())
]