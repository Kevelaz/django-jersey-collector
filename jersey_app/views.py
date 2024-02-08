from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Jersey, Team,Club
from .serializers import JerseySerializer, TeamSerializer, ClubSerializer, UserSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the jersey-collector api home route!'}
    return Response(content)

class JerseyList(generics.ListCreateAPIView):
  serializer_class = JerseySerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Jersey.objects.filter(user=user)
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class JerseyDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = JerseySerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Jersey.objects.filter(user=user)

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
  def perform_update(self, serializer):
    jersey = self.get_object()
    if jersey.user != self.request.user:
      raise PermissionDenied({"message":"You do not have permission to edit this cat"})
    serializer.save()
  
  def perform_destroy(self, instance):
    if instance.user != self.request.user:
      raise PermissionDenied({"message": "You do not have permission to delete this cat"})

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

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })