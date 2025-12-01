from django.urls import path, include
from .views import EscuderiaListView, EscuderiaCreateView, EscuderiaUpdateView, EscuderiaDeleteView, EscuderiaDetailView

app_name = 'escuderias' 

urlpatterns = [
    path('list/', EscuderiaListView.as_view(), name='escuderia_list'),
    path('create/', EscuderiaCreateView.as_view(), name='escuderia_create'),
    path('detail/<int:pk>/', EscuderiaDetailView.as_view(), name='escuderia_detail'),
    path('update/<int:pk>/', EscuderiaUpdateView.as_view(), name='escuderia_update'),
    path('delete/<int:pk>/', EscuderiaDeleteView.as_view(), name='escuderia_delete'),
    path('api/', include('escuderias.api.urls')),
]