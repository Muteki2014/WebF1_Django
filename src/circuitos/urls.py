from django.urls import path, include
from .views import CircuitoListView, CircuitoCreateView, CircuitoUpdateView, CircuitoDeleteView, CircuitoDetailView 

app_name = 'circuitos'

urlpatterns = [
    path('list/', CircuitoListView.as_view(), name='circuito_list'),
    path('create/', CircuitoCreateView.as_view(), name='circuito_create'),
    path('detail/<int:pk>/', CircuitoDetailView.as_view(), name='circuito_detail'),
    path('update/<int:pk>/', CircuitoUpdateView.as_view(), name='circuito_update'),
    path('delete/<int:pk>/', CircuitoDeleteView.as_view(), name='circuito_delete'),
    path('api/', include('circuitos.api.urls')),
]