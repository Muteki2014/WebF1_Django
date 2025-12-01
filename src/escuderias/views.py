from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Escuderia   


# Create your views here.

class EscuderiaListView(ListView):
    model = Escuderia
    template_name = 'escuderias/escuderia_list.html'
    context_object_name = 'escuderias'
    
    def get_queryset(self):
        q = self.request.GET.get("q", "")
        qs = Escuderia.objects.all()

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
    
class EscuderiaCreateView(LoginRequiredMixin, CreateView):
    model = Escuderia
    template_name = 'escuderias/escuderia_form.html'
    fields = ['nombre', 'pais', 'jefe_equipo', 'puntos', 'activo', 'foto']
    success_url = '/escuderias/list/'  
    context_object_name = 'escuderia'    
    
class EscuderiaDetailView(DetailView):
    model = Escuderia
    template_name = 'escuderias/escuderia_detail.html'
    context_object_name = 'escuderia'
    
    
class EscuderiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Escuderia
    template_name = 'escuderias/escuderia_form.html'
    fields = ['nombre', 'pais', 'jefe_equipo', 'puntos', 'activo', 'foto']
    success_url = '/escuderias/list/'  
    context_object_name = 'escuderia'
    
    
class EscuderiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Escuderia
    template_name = 'escuderias/escuderia_confirm_delete.html'
    success_url = '/escuderias/list/'  
    context_object_name = 'escuderia'
    
    
    
             
    
