from django.urls import path
from Entregable1 import views

urlpatterns = [
    path('/saludo', views.saludo),
    path('/login', views.testTemplate),
    path('', views.mainTemplate)
]