from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Jersey, Team,Club
from .serializers import JerseySerializer, TeamSerializer, ClubSerializer

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

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    clubs_not_associated = Club.objects.exclude(id__in=instance.clubs.all())
    clubs_serializer = ClubSerializer(clubs_not_associated, many=True)

    return Response({
        'jersey': serializer.data,
        'clubs_not_associated': clubs_serializer.data
    })

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

class ClubListCreate(generics.ListCreateAPIView):
  queryset = Club.objects.all()
  serializer_class = ClubSerializer

class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Club.objects.all()
  serializer_class = ClubSerializer
  lookup_field = 'id'

class AddClubToJersey(APIView):
  def post(self, request, jersey_id, club_id):
    jersey = Jersey.objects.get(id=jersey_id)
    club = Club.objects.get(id=club_id)
    jersey.clubs.add(club)
    return Response({'message': f'{club.name} added to Jersey info {jersey.name}'})