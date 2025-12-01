from django.urls import path
from .views import EscuderiaListAPI, EscuderiaDetailAPI

urlpatterns = [
    path('', EscuderiaListAPI.as_view(), name='escuderia_api_list'),
    path('<int:pk>/', EscuderiaDetailAPI.as_view(), name='escuderia_api_detail'),
]
