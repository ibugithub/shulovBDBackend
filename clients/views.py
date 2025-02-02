# clients/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework.decorators import api_view



class ClientCreateView(APIView):
  def post(self, request, format=None):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      

class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer


@api_view(['DELETE'])
def delete_client(request, client_id):
  try:
    client = Client.objects.get(id=client_id)
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  except Client.DoesNotExist:
    return Response(
      {"error": "Client not found"},
      status=status.HTTP_404_NOT_FOUND
    )
    
    
    
    

@api_view(['PUT'])
def update_client(request, client_id):
  try:
    client = Client.objects.get(id=client_id)
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  except Client.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)