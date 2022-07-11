
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Player, Team, Position, Tablero
from .serializers import PlayerSerializer, TeamSerializer, PositionSerializer, TableroSerializer


class PlayerApiView(APIView):
    """
    API View de los jugadores
    """

    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'nombre': request.data.get('nombre'),
            'equipo': request.data.get('equipo'),
            'tr': request.data.get('tr'),
            'ta': request.data.get('ta'),
            'goles': request.data.get('goles'),
            'pj': request.data.get('pj'),
            'sueldo': request.data.get('sueldo'),
        }

        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamApiView(APIView):
    """
    API View de los Equipos
    """

    def get(self, request, *args, **kwargs):

        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'nombre': request.data.get('nombre'),
            'ciudad': request.data.get('ciudad'),
            'num_jugadores': request.data.get('num_jugadores'),
            'division': request.data.get('division'),
        }

        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionApiView(APIView):
    """
    API View de las Posiciones
    """

    def get(self, request, *args, **kwargs):

        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TableroApiView(APIView):
    """
    API View del tablero
    """
    def get(self, request, *args, **kwargs):
        
        tableros = Tablero.objects.all()
        serializer = TableroSerializer(tableros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'local': request.data.get('local'),
            'visitante': request.data.get('visitante'),
            'goles_local': request.data.get('goles_local'),
            'goles_visitante': request.data.get('goles_visitante'),
        }
        print(data)

        serializer = TableroSerializer(data=data)
        if serializer.is_valid():

            tablero_instance = serializer.save()
            print(tablero_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
