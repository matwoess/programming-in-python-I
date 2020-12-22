"""
ex11.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 11
"""
import numpy as np


def __get_next_state__(state: np.ndarray) -> np.ndarray:
    neighbors = np.zeros(shape=state.shape, dtype=np.int)
    neighbors[1:] += state[:-1]  # propagate down
    neighbors[:-1] += state[1:]  # propagate up
    neighbors[:, 1:] += state[:, :-1]  # propagate right
    neighbors[:, :-1] += state[:, 1:]  # propagate left
    neighbors[1:, 1:] += state[:-1, :-1]  # propagate down-right
    neighbors[1:, :-1] += state[:-1, 1:]  # propagate down-left
    neighbors[:-1, :-1] += state[1:, 1:]  # propagate up-left
    neighbors[:-1, 1:] += state[1:, :-1]  # propagate up-right

    new_cells = state == 1
    survivor_cells = neighbors == 2
    born_cells = neighbors == 3
    new_cells &= survivor_cells
    new_cells |= born_cells
    return np.where(new_cells, 1, 0)
