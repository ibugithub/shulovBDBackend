# clients/urls.py
from django.urls import path
from .views import ClientCreateView, ClientListView, delete_client, update_client

urlpatterns = [
  path('register/', ClientCreateView.as_view(), name='client-create'),
  path('getClients/', ClientListView.as_view(), name='client-list'),
  path('deleteClient/<int:client_id>/', delete_client, name='client-delete'),
  path('updateClient/<int:client_id>/', update_client, name='client-update')
]