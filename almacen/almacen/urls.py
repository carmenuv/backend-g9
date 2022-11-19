# seria como la guia telefónica entera de todo nuestro proyecto
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluimos todas las rutas definidas en el archivo urls de la APLICACION ne nuestro proyecto
    path('gestion/', include('gestion.urls'))
]
