from django.urls import path
from .views import *
# Me genera tood el proceso de autenticaión (valida si el usurio es correcto) y además me genera la token de acceso y la token de refresco
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
  path('registro/', RegistroUsuarioApiView.as_view()),
  path('platos/', PlatosApiView.as_view()),
  path('plato-toggle/<str:id>', PlatoToggleApiView.as_view()),
  path('plato/<int:pk>', PlatoUpdateApiView.as_view()),
  path('iniciar-sesion/', TokenObtainPairView.as_view()),
  path('platos-protegido/', VistaProtegidaPlatosApiView.as_view()),
]