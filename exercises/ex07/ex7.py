"""
ex7.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 7
"""
from typing import List, Tuple


def get_file_metadata(data_as_string: str) -> Tuple[str, int, List[str]]:
    lines = [line for line in data_as_string.split('\n') if line.strip()]
    header_start = '% SeqHeadStart'
    header_end = '% SeqHeadEnd'
    data_end = '% End of data'
    header_start_idx = header_end_idx = data_end_idx = None
    for i, l in enumerate(lines):
        if header_start_idx is None and not l.startswith(header_start):
            raise AttributeError('file does not start with header')
        if l.startswith(header_start):
            header_start_idx = i
        elif l.startswith(header_end):
            header_end_idx = i
        elif l.startswith(data_end):
            data_end_idx = i
        if data_end_idx:
            break

    if not all(elem is not None for elem in [header_start_idx, header_end_idx, data_end_idx]):
        raise AttributeError('missing tags in file')
    if not header_start_idx < header_end_idx < data_end_idx:
        raise AttributeError('invalid file structure')

    id_col = '% ID:'
    date_col = '% Date:'
    columns_col = '% Columns:'
    header_lines = lines[header_start_idx + 1: header_end_idx]
    id_col_idx = date_col_idx = columns_col_idx = None
    for i, l in enumerate(header_lines):
        if not l.startswith('%'):
            raise AttributeError('invalid row in header')
        if l.startswith(id_col):
            id_col_idx = i
        elif l.startswith(date_col):
            date_col_idx = i
        elif l.startswith(columns_col):
            columns_col_idx = i
    if not all(elem is not None for elem in [id_col_idx, date_col_idx, columns_col_idx]):
        raise AttributeError('missing header entries')

    id = header_lines[id_col_idx][len(id_col):].strip()
    date = header_lines[date_col_idx][len(date_col):].strip()
    columns = header_lines[columns_col_idx][len(columns_col):].strip()
    try:
        date = int(date)
    except (ValueError, TypeError):
        raise TypeError('could not convert date value to integer value')
    columns = columns.split(';')

    return id, date, columns
