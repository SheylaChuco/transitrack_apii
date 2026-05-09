from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        RutaListCreateView.as_view()
    ),

    path(
        '<int:pk>/',
        RutaDetailView.as_view()
    ),
]