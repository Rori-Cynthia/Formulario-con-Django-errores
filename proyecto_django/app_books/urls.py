from django.urls import path
from . import views

urlpatterns = [
    path('inputbook/', views.input_book, name='inputbook'),
]
