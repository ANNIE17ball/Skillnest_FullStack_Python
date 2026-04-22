"""
Evaluacion core
"""
# 1) --------------------------------------------------------------------------------------------------------------------
# En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda).
# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
# En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
# En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).

# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600

print(puntajes)
# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers["nombre"]
print(streamers)
# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

print(eventos)
# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

print(ubicacion)