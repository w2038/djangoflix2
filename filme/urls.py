from django.urls import path, include
from .views import Detalhesfilmes, Homepage, Homefilmes, Pesquisafilme
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name = 'homepage'),
    path('filmes/', Homefilmes.as_view(), name = 'homefilmes'),
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
]