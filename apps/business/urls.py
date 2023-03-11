from django.urls import path
from apps.business.views import *

urlpatterns = [
        path('category-business/', CategoryAPIView.as_view(), name='category-business'),
        path('business-detail-post/', BusinessDetailPostAPIView.as_view(), name='business-detail-post'),
        path('business-detail-update/<int:pk>/', BusinessDetailUpdateAPIView.as_view(), name='business-detail-update'),
        path('business-detail-get/<int:pk>/', BusinessDetailGetAPIView.as_view(), name='business-detail-get')
]
