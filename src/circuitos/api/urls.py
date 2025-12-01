from django.urls import path
from .views import CircuitoListAPI, CircuitoDetailAPI

urlpatterns = [
    path('', CircuitoListAPI.as_view(), name='circuito_api_list'),
    path('<int:pk>/', CircuitoDetailAPI.as_view(), name='circuito_api_detail'),
]
