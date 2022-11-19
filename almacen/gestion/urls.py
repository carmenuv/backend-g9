# Aca definiremos todas las rutas que tendrá acceso nuestra aplicación

from django.urls import path
from .views import saludar, parametros, PruebaApiView

# Tenemos que crear esta variable NO SE PUEDE LLAMAR DE OTRA MANERA
urlpatterns = [
  path('inicio/', saludar),
  path('parametros/<str:nombre>', parametros),
  # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
  path('prueba/', PruebaApiView.as_view())
]