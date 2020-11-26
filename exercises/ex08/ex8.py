"""
ex8.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 8
"""

import numpy as np
import pandas as pd

from argparse import ArgumentParser

from exercises.ex05.ex5 import count_bases_and_subsequence
from exercises.ex06.ex6 import get_hamsters
from exercises.ex07.ex7 import get_file_metadata

parser = ArgumentParser()
parser.add_argument('input_folder', help='the input folder', type=str)
parser.add_argument('output_file', help='the output file', type=str)
parser.add_argument('subsequence', help='the subsequence', type=str)

args = parser.parse_args()
input_folder = args.input_folder
output_file = args.output_file
subsequence = args.subsequence

hamsters = get_hamsters(input_folder)
stats = np.zeros(shape=(200, 5), dtype=np.float64)
for _, file_content in hamsters:
    subsequence_count, occurrences = count_bases_and_subsequence(file_content, subsequence)
    hamster_id, date, _ = get_file_metadata(file_content)
    stats[date] += np.array([subsequence_count, *occurrences.values()])
stats /= 20
df = pd.DataFrame(stats, columns=['subsequence', 'a', 'c', 'g', 't'])
df.to_csv(output_file, sep=' ', index=False)
