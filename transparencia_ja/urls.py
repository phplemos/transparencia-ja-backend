from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls' )),  # Inclui as URLs do app 'users' sob o prefixo /api/
    path('api/', include('posts.urls' )),
    path('api/', include('contratantes.urls' )),
    path('api/', include('comentarios.urls' )),
]
