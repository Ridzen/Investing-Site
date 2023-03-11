from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.views import *


router = DefaultRouter()

router.register('business_owner', BusinessOwnerViewSet, basename='business_owner')


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', Authorization.as_view(), name='login'),
    path('userinfo/', UserAPI.as_view(), name='userinfo'),

    path('investors/', InvestorListView.as_view(), name='investor_list'),
    path('investors/<int:pk>/', InvestorDetailView.as_view(), name='investor_detail'),

]
