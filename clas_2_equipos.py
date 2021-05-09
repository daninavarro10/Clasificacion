from bt_scheme import PartialSolution, BacktrackingSolver, State, Solution
from typing import *


def clasification_solve(puntos_a, puntos_b, partidos):
    class ClasificationPS(PartialSolution):
        def __init__(self, puntos_a, puntos_b, n):
            self.puntos_a = puntos_a
            self.puntos_b = puntos_b
            self.partidos = partidos
            self.n = n  # para recorrer partidos

        def is_solution(self) -> bool:
            return self.n == len(partidos) # cuando haya recorrido todos los partidos

        def get_solution(self) -> Solution:
            return self.puntos_a, self.puntos_b

        def successors(self) -> Iterable["ClasificationPS"]:  # IMPLEMENTAR
            # recorro partidos
            # para cada partido hay 3 posibles soluciones
            if self.n < len(partidos):
                yield ClasificationPS(self.puntos_a + 3, self.puntos_b + 0, self.n + 1)
                yield ClasificationPS(self.puntos_a + 1, self.puntos_b + 1, self.n + 1)
                yield ClasificationPS(self.puntos_a + 0, self.puntos_b + 3, self.n + 1)

    return BacktrackingSolver.solve(ClasificationPS(puntos_a, puntos_b, 0))


# Programa principal ------------------------------------------
if __name__ == "__main__":

    partidos = [(0, 1), (1, 0)]
    puntos_a, puntos_b = 0, 0

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

    for sol in clasification_solve(puntos_a, puntos_b, partidos):
        print(sol)
    print("\n<TERMINADO>")
