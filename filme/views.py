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