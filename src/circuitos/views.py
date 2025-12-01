from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Circuito

# Create your views here.

class CircuitoListView(ListView):
    model = Circuito
    template_name = 'circuitos/circuito_list.html'
    context_object_name = 'circuitos'  
    
    def get_queryset(self):
        q = self.request.GET.get("q", "")
        qs = Circuito.objects.all()

        if q:
            qs = qs.filter(
                Q(pais__icontains=q) |
                Q(nombre__icontains=q)
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q", "")
        return context
    

class CircuitoCreateView(LoginRequiredMixin, CreateView):   
    model = Circuito
    template_name = 'circuitos/circuito_form.html'
    fields = ['nombre', 'pais', 'longitud_km', 'vueltas', 'record_vuelta', 'foto']
    success_url = '/circuitos/list/'  
    context_object_name = 'circuito'    
    
    
class CircuitoDetailView(DetailView):
    model = Circuito
    template_name = 'circuitos/circuito_detail.html'
    context_object_name = 'circuito'
    
    
class CircuitoUpdateView(LoginRequiredMixin, UpdateView):
    model = Circuito
    template_name = 'circuitos/circuito_form.html'
    fields = ['nombre', 'pais', 'longitud_km', 'vueltas', 'record_vuelta', 'foto']
    success_url = '/circuitos/list/'  
    context_object_name = 'circuito'
    
    
class CircuitoDeleteView(LoginRequiredMixin, DeleteView):
    model = Circuito
    template_name = 'circuitos/circuito_confirm_delete.html'
    success_url = '/circuitos/list/'  
    context_object_name = 'circuito'                
    
    

    