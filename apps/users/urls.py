from django.urls import path
from .views import *
from apps.common.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),

    path("create-content/", CreateContentView.as_view()),
    path("create-category/", CreateCategoryView.as_view()),

    path('contents/', ContentListView.as_view(), name='content-list')
]