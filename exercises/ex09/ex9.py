"""
ex9.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 9
"""

import sys
import subprocess
import shutil
from pathlib import Path
from argparse import ArgumentParser

from exercises.ex09.plot_csv import plot_csv

parser = ArgumentParser()
parser.add_argument('output_folder', help='the output folder', type=str)
args = parser.parse_args()
output_folder = args.output_folder

folder_path = Path(output_folder)
folder_path.mkdir(exist_ok=True)
sub_folder_path = Path(output_folder).joinpath('200')
if sub_folder_path.exists():
    shutil.rmtree(sub_folder_path)
sub_folder_path.mkdir()
subprocess.call([sys.executable, './hamstergenegen.py', sub_folder_path])
subprocess.call([sys.executable, '../ex08/ex8.py', folder_path, folder_path / 'patterns_analysis.csv', 'ctag'])
plot_csv(folder_path / 'patterns_analysis.csv', folder_path / 'patterns_analysis.png')
