from django.urls import path

from . import views #Importo las vistas
 
urlpatterns = [ #para definir las asociaciones entre las URLs de la aplicación web y las vistas que se encargan de manejar esas URLs.
    path("", views.index, name="index"),
]