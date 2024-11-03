from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('jogos/', views.jogos),
    path('sobre/', views.sobre),
    path('asset/', views.asset)
]
