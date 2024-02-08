from django.urls import path
# import Home view from the views file
from .views import Home, JerseyList, JerseyDetail, TeamListCreate, TeamDetail, ClubListCreate, ClubDetail, AddClubToJersey, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('jerseys/', JerseyList.as_view(), name='jersey-list'),
  path('jerseys/<int:id>/', JerseyDetail.as_view(), name='jersey-detail'),
  path('jerseys/<int:jersey_id>/teams/', TeamListCreate.as_view(), name='team-list-create'),
	path('jerseys/<int:jersey_id>/teams/<int:id>/', TeamDetail.as_view(), name='team-detail'),
  path('clubs/', ClubListCreate.as_view(), name='club-list-create'),
  path('clubs/<int:id>/', ClubDetail.as_view(), name='club-detail'),
  path('jerseys/<int:jersey_id>/add_club/<int:club_id>/', AddClubToJersey.as_view(), name='add-club-to-jersey'),
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(),name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]

