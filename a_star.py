#!/usr/bin/env python
"""
Curso de Especialização de Inteligência Artificial Aplicada
Setor de Educação Profissional e Tecnológica - SEPT
Universidade Federal do Paraná - UFPR

IAA003 - Linguagem de Programação Aplicada
Prof. Alexander Robert Kutzke

Exercício de implementação do Algoritmo A*.
"""


import sys
from copy import copy

import dists

__author__ = "Patrick Rodrigues"
__version__ = "0.0.1"
__email__ = "patrick.pwall@gmail.com"

MAX_INT = sys.maxsize


# goal sempre sera 'bucharest'
def a_star(
    city: str,
    border: list = None,
    total_distance: int = 0,
    path: list = None,
    goal: str = "Bucharest",
):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    if city == goal:
        return path + ["Bucharest"]

    if border is None:
        border = []

    if path is None:
        path = []
    else:
        path = copy(path)

    path.append(city)
    for border_city, distance in dists.dists[city]:
        g = distance + total_distance
        h = dists.straight_line_dists_from_bucharest[border_city]
        f = g + h  # Evaluation Function
        border.append((g, h, f, border_city, path))

    smallest_cost = MAX_INT
    index = None
    for i, (g, h, f, c, p) in enumerate(border):
        if f < smallest_cost:
            smallest_cost = f
            city = c
            total_distance = g
            index = i
            path = p

    border.pop(index)

    return a_star(city, border, total_distance, path)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        city = sys.argv[1]
        if city not in dists.dists:
            print("Invalid city. Please, try again...")
            sys.exit()
    else:
        city = "Lugoj"
    path_list = a_star(city)
    print(path_list)
