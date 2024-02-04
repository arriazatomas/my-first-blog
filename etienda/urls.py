from django.urls import path
from . import views

urlpatterns = [
    path('',views.productos, name='productos'),
    path('producto/<int:pk>/', views.producto_detallado, name='producto_detallado'),
]