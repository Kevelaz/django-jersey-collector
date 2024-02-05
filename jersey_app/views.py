from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Jersey
from .serializers import JerseySerializer

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
