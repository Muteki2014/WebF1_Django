from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Piloto

# Create your views here.
class PilotoListView(ListView):
    model = Piloto
    template_name = 'pilotos/piloto_list.html'
    context_object_name = 'pilotos'
    
    def get_queryset(self):
        q = self.request.GET.get("q", "")
        qs = Piloto.objects.all()

        if q:
            qs = qs.filter(
                Q(nombre__icontains=q) |
                Q(apellido__icontains=q) |
                Q(nacionalidad__icontains=q) |
                Q(numero__icontains=q) |
                Q(escuderia__icontains=q)
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q", "")
        return context
    
    
class PilotoCreateView(LoginRequiredMixin, CreateView):
    model = Piloto
    template_name = 'pilotos/piloto_form.html'
    fields = ['nombre', 'apellido', 'nacionalidad','fecha_nacimiento', 'numero', 'escuderia', 'puntos', 'activo', 'foto']
    success_url = '/pilotos/list/'  
    context_object_name = 'piloto'  
    
    
class PilotoDetailView(DetailView):
    model = Piloto
    template_name = 'pilotos/piloto_detail.html'
    context_object_name = 'piloto'    
    
    
class PilotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Piloto
    template_name = 'pilotos/piloto_form.html'
    fields = ['nombre', 'apellido', 'nacionalidad','fecha_nacimiento', 'numero', 'escuderia', 'puntos', 'activo', 'foto']
    success_url = '/pilotos/list/'  
    context_object_name = 'piloto'  
    
    
class PilotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Piloto
    template_name = 'pilotos/piloto_confirm_delete.html'
    success_url = '/pilotos/list/'  
    context_object_name = 'piloto'      