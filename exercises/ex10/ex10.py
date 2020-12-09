"""
ex10.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 10
"""
import re
from typing import Tuple
import numpy as np
from pathlib import Path


def read_config_file(configpath: str) -> Tuple[int, str, str, np.ndarray]:
    config = Path(configpath)
    content = config.read_text()
    match = re.search(r'n_iterations:\s*(.*)\s*', content)
    if not match:
        raise AttributeError('no config entry for "n_iterations" found or not in the right format.')
    try:
        n_iterations = int(match.group(1))
    except (ValueError, TypeError):
        raise AttributeError('couldn\'t convert "n_iterations" value to integer.')
    match = re.search(r'dead_symbol:\s*"(.)"', content)
    if not match:
        raise AttributeError('no config entry for "dead_symbol" found or invalid amount of characters.')
    dead_symbol = match.group(1)
    match = re.search(r'live_symbol:\s*"(.)"', content)
    if not match:
        raise AttributeError('no config entry for "live_symbol" found or invalid amount of characters.')
    live_symbol = match.group(1)
    match = re.search(r'init_state:\s*\n"\n([^")]+)', content)
    if not match:
        raise AttributeError('no config entry for "init_state" or invalid characters in it.')
    init_state_string = match.group(1)
    if not set(init_state_string).issubset({dead_symbol, live_symbol, '\n'}):
        raise ValueError('invalid characters found in "init_state"')
    int_state_list = init_state_string.splitlines()
    if len({len(item) for item in int_state_list}) != 1:
        raise ValueError('length of each line in "init_state" must be equally long')
    init_state = np.array([list(row) for row in int_state_list])
    init_state = np.where(init_state == live_symbol, 1, 0)
    return n_iterations, dead_symbol, live_symbol, init_state
