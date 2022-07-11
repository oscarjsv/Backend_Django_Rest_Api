
# API REST 

Una Api Rest en la que puedes ingresar equipos y jugadores tambien agregar un marcador y ver la posicion de esos equipos en la tabla de posiciones

## Tech Stack

**Server:** Python, Django, Docker, React

## Alerta -

Es necesario no tener estos puertos  **80**, **8080** en uso

  
  
- credenciales admin Django


- oscar

- 1234


  
## correr en local

Clona el repositorio

Falta
```bash
  git clone 'https://github.com/oscarjsv/Frontend_React_Django_Rest_Api.git'
```

Ir al directorio del proyecto

Falta
```bash
  cd Backend_Django_Rest_Api
```

Install Docker

Start the server

```bash
docker-compose up --build  --remove-orphans
```

  
## API Reference

#### GET jugadores

```http
  GET http://127.0.0.1/api/player-view

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `string, integer` | **Required**. api para Obtener todos los jugadores |

#### POST Jugador

```http
  POST http://127.0.0.1/api/player-view
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id, nombre, equipo, tr, ta, goles, pj, sueldo`      | `string, array, integer` | **Required**. campos del jugador que se registrará en un equipo |


#### GET Equipos

```http
  GET http://127.0.0.1/api/team-view
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `None`      | `string, integer` | **Required**. Api para Obtener todos los Equipos |

#### POST Equipo

```http
  POST http://127.0.0.1/api/team-view
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id, nombre, ciudad, num_jugadores, division`      | `string, array, integer` | **Required**. Campo del equipo a registrar |

#### POST Tablero

```http
  POST http://127.0.0.1/api/tablero-view
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `local, visitante, goles_local, goles_visitante`      | `string, integer` | **Required**. Api para Obtener los goles y equipos tanto como el perdedor como el visitante |

#### GET Position

```http
  GET http://127.0.0.1/api/position-view
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `equipo, pj, pg, pp, goles, puntos`      | `string, integer` | **Required**. Api para ver las estadistica de todos los equipos |





  
## Autor

- [@oscarjsv](https://www.github.com/oscarjsv)