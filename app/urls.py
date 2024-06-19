from django.urls import path
from .views import CarViewSet

urlpatterns = [
    path('car/', CarViewSet.as_view({'get': 'list'}), name='car')
]
