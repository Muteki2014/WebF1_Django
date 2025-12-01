from django.urls import path, include
from .views import PilotoListView, PilotoCreateView, PilotoUpdateView, PilotoDeleteView, PilotoDetailView   

app_name = 'pilotos'

urlpatterns = [
    path('list/', PilotoListView.as_view(), name='piloto_list'),
    path('create/', PilotoCreateView.as_view(), name='piloto_create'),
    path('detail/<int:pk>/', PilotoDetailView.as_view(), name='piloto_detail'),
    path('update/<int:pk>/', PilotoUpdateView.as_view(), name='piloto_update'),
    path('delete/<int:pk>/', PilotoDeleteView.as_view(), name='piloto_delete'),
    path('api/', include('pilotos.api.urls')),
]
