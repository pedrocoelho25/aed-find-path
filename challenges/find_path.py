import heapq
from data_structures.city_map import CityMap


def estimar_distancia(city_map, atual, objetivo):
    return 0


def reconstruir_caminho(anterior, inicio, objetivo):
    caminho = []
    atual = objetivo

    while atual != inicio:
        caminho.append(atual)
        atual = anterior[atual]

    caminho.append(inicio)
    caminho.reverse()

    return caminho


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if start not in city_map.intersections:
        return []

    if goal not in city_map.intersections:
        return []

    if start == goal:
        return [start]

    fila_prioridade = []

    heapq.heappush(fila_prioridade, (0, start))

    custo_ate_agora = {}
    custo_ate_agora[start] = 0

    anterior = {}

    visitados = set()

    while len(fila_prioridade) > 0:
        prioridade_atual, atual = heapq.heappop(fila_prioridade)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == goal:
            return reconstruir_caminho(anterior, start, goal)

        vizinhos = city_map.roads[atual]

        for vizinho in vizinhos:
            novo_custo = custo_ate_agora[atual] + 1

            if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:
                custo_ate_agora[vizinho] = novo_custo

                anterior[vizinho] = atual

                estimativa = estimar_distancia(city_map, vizinho, goal)

                prioridade = novo_custo + estimativa

                heapq.heappush(fila_prioridade, (prioridade, vizinho))

    return []
