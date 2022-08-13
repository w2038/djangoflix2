from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> lista de itens do modelo

class Detalhesfilmes(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # objetc -> um item do nosso modelo 
    
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(request, *args, **kwargs) #redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context