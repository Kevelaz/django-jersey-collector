from django.urls import path
# import Home view from the views file
from .views import Home, JerseyList, JerseyDetail, TeamListCreate, TeamDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('jerseys/', JerseyList.as_view(), name='jersey-list'),
  path('jerseys/<int:id>/', JerseyDetail.as_view(), name='jersey-detail'),
  path('jerseys/<int:jersey_id>/teams/', TeamListCreate.as_view(), name='team-list-create'),
	path('jerseys/<int:jersey_id>/teams/<int:id>/', TeamDetail.as_view(), name='team-detail'),
]

