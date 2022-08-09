from django.urls import path, include
from .views import Detalhesfilmes, Homepage, Homefilmes


urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    path('filmes/<int:pk>', Detalhesfilmes.as_view())
]