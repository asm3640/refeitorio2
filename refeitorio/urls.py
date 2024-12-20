"""
URL configuration for refeitorio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from refeitorioApp.views import opcoes_views, new_aluno,editar_aluno, excluir_aluno, cadastrar_evento, editar_evento, excluir_evento

urlpatterns = [
    path('', opcoes_views, name='opcoes_views'),
    path('admin/', admin.site.urls),
    
    path('new_aluno/',new_aluno, name='new_aluno'),
    path('editar_aluno/<str:id>', editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<str:id>', excluir_aluno, name='excluir_aluno'),
    
    path('cadastrar_evento/', cadastrar_evento, name='cadastrar_evento'),
    path('editar_evento/<str:id>', editar_evento, name='editar_evento'),
    path('excluir_evento/<str:id>', excluir_evento, name='excluir_evento'),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
