from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    if problem.isGoalState(state):
        return 0
    
    posiscion, survivors_grid = state
    
    supervivientes = []
    for m in range(len(survivors_grid)):
        for n in range(len(survivors_grid[m])):
            if survivors_grid[m][n]:
                supervivientes.append((m, n))
    
    menor = float("inf")
    x1, y1 = posiscion
    for pos in range(len(supervivientes)):
        x2, y2 = supervivientes[pos]
        cordenada_x = abs(x1 - x2)
        cordenada_y = abs(y1 - y2)
        distancia_manhattan = cordenada_x + cordenada_y
        if distancia_manhattan < menor:
            menor = distancia_manhattan

    if len(supervivientes) == 1:
        return menor

    visitados = set()
    mst_costo = 0
    
    visitados.add(supervivientes[0])
    
    while len(visitados) < len(supervivientes):
        distancia_corta = float("inf")
        super_cercano = None
        
        for visitado in visitados:
            for superviviente in supervivientes:
                if superviviente not in visitados:
                    x1_1 , y1_2 = visitado
                    x2_1 , y2_2 = superviviente
                    cordenada_x = abs(x1_1 - x2_1)
                    cordenada_y = abs(y1_2 - y2_2)
                    distancia_manhattan = cordenada_x + cordenada_y
                    if distancia_manhattan < distancia_corta:
                        distancia_corta = distancia_manhattan
                        super_cercano = superviviente  
                    
        visitados.add(super_cercano)
        mst_costo += distancia_corta
    
    return menor + mst_costo
    
