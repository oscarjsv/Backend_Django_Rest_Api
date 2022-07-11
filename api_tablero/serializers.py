from rest_framework import serializers
from .models import Player, Team, Position, Tablero


class PlayerSerializer(serializers.ModelSerializer):
    '''
    En esta clase se crea el serializador de nuestro modelo Player
    '''

    class Meta:
        model = Player
        fields = ['id', 'nombre', 'equipo',
                  'tr', 'ta', 'goles', 'pj', 'sueldo']


class TeamSerializer(serializers.ModelSerializer):
    '''
    En esta clase se crea el serializador de nuestro modelo Team
    '''

    class Meta:
        model = Team
        fields = ['nombre', 'ciudad', 'num_jugadores', 'division']


class PositionSerializer(serializers.ModelSerializer):
    '''
    En esta clase se crea el serializador de nuestro modelo Position
    '''
    class Meta:
        model = Position
        fields = ['equipo',
                  'pj', 'pg', 'pp', 'goles', 'puntos']


class TableroSerializer(serializers.ModelSerializer):
    '''
    En esta clase se crea el serializador de nuestro modelo Tablero y 
    sobreescribir el metodo create para poder modificar y obtener los datos de mi
    modelo Tablero y por ingresar la información en Position
    '''
    class Meta:
        model = Tablero
        fields = ['local', 'visitante', 'goles_local', 'goles_visitante']

    def _upsert(self, nombre_equipo, pp, pj, pg, goles, puntos):
        """
        a este metodo le paso todos los parametros que se requieren para crear la persistencia de 
        de los datos que se necesitan en Position, tanto como para el ganador como para el perdedor y 
        si en algún caso hay empate
        """
        if Position.objects.filter(equipo=nombre_equipo):
            equipo = Position.objects.filter(
                equipo=nombre_equipo).first()
            equipo.pg += pg
            equipo.pj += pj
            equipo.pp += pp
            equipo.goles += goles
            equipo.puntos += puntos
            equipo.save()
        else:
            Position.objects.create(
                equipo=nombre_equipo, pj=pj, pg=pg, pp=pp, goles=goles, puntos=puntos)

    def create(self, validated_data):
        local = validated_data['local']
        visitante = validated_data['visitante']
        goles_local = validated_data['goles_local']
        goles_visitante = validated_data['goles_visitante']

        if goles_local == goles_visitante:
            self._upsert(local, 0, 1, 0, goles_local, 1)
            self._upsert(visitante, 0, 1, 0, goles_visitante, 1)

            return Tablero.objects.create(**validated_data)

        data = {'nombre_ganador': local, 'nombre_perdedor': visitante,
                'goles_ganador': goles_local, 'goles_perdedor': goles_visitante}

        if goles_visitante > goles_local:
            data['nombre_ganador'] = visitante
            data['goles_ganador'] = goles_visitante
            data['nombre_perdedor'] = local
            data['goles_perdedor'] = goles_local

        self._upsert(data["nombre_ganador"], 0, 1, 1, data["goles_ganador"], 3)
        self._upsert(data["nombre_perdedor"], 1, 1,
                     0, data["goles_perdedor"], 0)

        return Tablero.objects.create(**validated_data)
