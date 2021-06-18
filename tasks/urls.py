from django.urls import path
from .import views

urlpatterns=[

    path('add/',views.home),
    path('remove/',views.removeTask)
]