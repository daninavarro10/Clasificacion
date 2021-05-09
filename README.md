# Clasificacion

Dado unos equipos con sus respectivos puntos y una lista de partidos queremos recorrer todas las posibilidades de los equipos.

En la primera versión se han utilizado 2 equipos y 2 partidos con la puntuación inicial de ambos equipos igual a 0.

puntos_equipo_a, puntos_equipo_b = 0, 0
partidos = [(0,1), (1,0)] # equipo 0 vs equipo 1 y equipo 1 vs equipo 0

Está sería la solución deseada (victoria 3 puntos, empate 1 punto, derrota 0 puntos):

    # 2 partidos y 3 posibilidades por partido (1, X, 2) = 3² = 9 total
    # (3,0), (3,0) = (6,0)
    # (3,0), (1,1) = (4,1)
    # (3,0), (0,3) = (3,3)
    # (0,3), (0,3) = (0,6)
    # (0,3), (3,0) = (3,3)
    # (0,3), (1,1) = (1,4)
    # (1,1), (3,0) = (4,1)
    # (1,1), (1,1) = (2,2)
    # (1,1), (0,3) = (1,4)

Y esta la solución obtenida:
(6, 0)
(4, 1)
(3, 3)
(4, 1)
(2, 2)
(1, 4)
(3, 3)
(1, 4)
(0, 6)
    
En la segunda versión se utilizan valores reales:
# 10 equipos:
equipos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3 jornadas, 5 partidos por jornada
partidos = [(9, 8), (5, 1), (3, 2), (0, 6), (4, 7),
            (2, 0), (1, 3), (8, 5), (7, 9), (6, 4),
            (3, 8), (0, 1), (4, 2), (9, 6), (5, 7)]


Como vemos, en el primer partido jugará el equipo 9 contra el equipo 8, en el segundo el equipo 5 contra el equipo 1, y así sucesivamente.

Habría 3¹⁵ posibles soluciones, para visualizar resultados se podrá reducir el número de partidos.









