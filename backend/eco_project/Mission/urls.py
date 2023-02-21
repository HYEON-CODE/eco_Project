from django.urls import path
from .views import MissionList, MissionDetail, CompletedMissionList

urlpatterns = [
    path('', MissionList.as_view()),
    path('<int:pk>/', MissionDetail.as_view()),
    path('complete/', CompletedMissionList.as_view(), name='completed-mission-create'),
]