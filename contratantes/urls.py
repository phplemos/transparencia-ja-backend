from django.urls import path
from .views import ContratanteList, ContratanteDetail

urlpatterns = [
    path('contratantes/', ContratanteList.as_view(), name='contratante_list'),
    path('contratantes/<int:id>/', ContratanteDetail.as_view(), name='contratante_detail'),
]
