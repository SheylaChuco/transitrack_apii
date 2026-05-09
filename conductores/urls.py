from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        ConductorListCreateView.as_view()
    ),

    path(
        '<int:pk>/',
        ConductorDetailView.as_view()
    ),
]