from django.db import models

# Modelo de los Equipos
class Team(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    ciudad = models.CharField(max_length=50)
    num_jugadores = models.IntegerField()
    division = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Modelo de los Jugadores
class Player(models.Model):
    nombre = models.CharField(max_length=50)
    equipo = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=False, blank=False)
    tr = models.IntegerField()
    ta = models.IntegerField()
    goles = models.IntegerField()
    pj = models.IntegerField()
    sueldo = models.IntegerField()

    def __str__(self):
        return self.nombre


# Modelo de la posicion de los equipos
class Position(models.Model):
    equipo = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True)
    pj = models.IntegerField(null=True,
                             blank=True)
    pg = models.IntegerField(null=True,
                             blank=True)
    pp = models.IntegerField(null=True,
                             blank=True)
    goles = models.IntegerField(null=True,
                                blank=True)
    puntos = models.IntegerField(null=True,
                                 blank=True)

    class Meta:
        ordering = ['puntos']


# Modelo del tablero
class Tablero(models.Model):
    local = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name='equipo_local')
    visitante = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name='equipo_visitante')
    goles_local = models.IntegerField(null=True,
                                      blank=True)
    goles_visitante = models.IntegerField(null=True,
                                          blank=True)
