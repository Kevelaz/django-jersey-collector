from django.urls import path
# import Home view from the views file
from .views import Home, JerseyList, JerseyDetail

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('jerseys/', JerseyList.as_view(), name='jersey-list'),
  path('jerseys/<int:id>/', JerseyDetail.as_view(), name='jersey-detail'),
]

