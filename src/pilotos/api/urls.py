from django.urls import path
from .views import PilotoListAPI, PilotoDetailAPI

urlpatterns = [
    path('', PilotoListAPI.as_view(), name='piloto_api_list'),
    path('<int:pk>/', PilotoDetailAPI.as_view(), name='piloto_api_detail'),
]
