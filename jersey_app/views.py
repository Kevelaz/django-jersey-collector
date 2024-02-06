from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Jersey, Team
from .serializers import JerseySerializer, TeamSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the jersey-collector api home route!'}
    return Response(content)

class JerseyList(generics.ListCreateAPIView):
  queryset = Jersey.objects.all()
  serializer_class = JerseySerializer

class JerseyDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Jersey.objects.all()
  serializer_class = JerseySerializer
  lookup_field = 'id'

class TeamListCreate(generics.ListCreateAPIView):
  serializer_class = TeamSerializer
  
  def get_queryset(self):
    jersey_id = self.kwargs['jersey_id']
    return Team.objects.filter(jersey_id=jersey_id)
  def perform_create(self, serializer):
    jersey_id = self.kwargs['jersey_id']
    jersey = Jersey.objects.get(id=jersey_id)
    serializer.save(jersey=jersey)

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = TeamSerializer
  lookup_field = 'id'

  def get_queryset(self):
    jersey_id = self.kwargs['jersey_id']
    return Team.objects.filter(jersey_id=jersey_id) 
