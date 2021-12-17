from django.contrib import admin
from django.urls import path
from entrega_1_project_coder.views import saludo, testTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('login/', testTemplate)
]
