"""
ex5.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 5
"""

import os
from typing import Tuple


def count_occurrences(data: list, valid: tuple, thresh: float) -> dict:
    occurrences = {}
    for v in valid:
        occurrences[v] = 0
    for _, base, quality in data:
        if base in valid and quality >= thresh:
            occurrences[base] += 1
    return occurrences


def count_subsequences(data: list, subsequence: str, thresh: float) -> int:
    base_sequence = ''.join(['_' if q < thresh else b for _, b, q in data])
    count = base_sequence.count(subsequence)
    return count


def count_bases_and_subsequence(data_as_string: str, subsequence: str) -> Tuple[int, dict]:
    # header_start = '% SeqHeadStart'
    header_end = '% SeqHeadEnd'
    data_end = '% End of data'
    sep = ';'
    comment = '%'
    invalid_tuple = '_;_;-1.0'
    lines = data_as_string.split('\n')
    data_section = lines[lines.index(header_end):lines.index(data_end)]
    data_lines = [line.lower() if (line.strip() and not line.startswith(comment)) else invalid_tuple
                  for line in data_section]
    data = [(info, base, float(quality))
            for info, base, quality in (tuple(line.split(sep))
                                        for line in data_lines)]
    occurrences = count_occurrences(data, ('a', 'c', 'g', 't'), 0.08)
    seq_count = count_subsequences(data, subsequence.lower(), 0.08)
    return seq_count, occurrences


if __name__ == '__main__':
    filename = os.path.join('00', 'data_00-000.raw.seq')
    path = '00/data_00-000.raw.seq'
    with open(filename, 'r') as fh:
        file_content = fh.read()
    subsequence_count, base_counts = count_bases_and_subsequence(data_as_string=file_content, subsequence="AcG")
    print('subsequence count:', subsequence_count)
    print('base counts:', base_counts)
