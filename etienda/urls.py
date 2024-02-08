from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.productos, name='productos'),
    path('producto/<int:pk>/', views.producto_detallado, name='producto_detallado'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)