from django.urls import path
from api_tablero import views


urlpatterns = [
    path('player-view', views.PlayerApiView.as_view()),
    path('team-view', views.TeamApiView.as_view()),
    path('position-view', views.PositionApiView.as_view()),
    path('tablero-view', views.TableroApiView.as_view()),
]