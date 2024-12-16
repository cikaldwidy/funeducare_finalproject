from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('fasilitas/<int:fasilitas_id>', views.detail_fasilitas, name='detail'),
    path('fasilitas/', views.fasilitas, name='fasilitas'),
]