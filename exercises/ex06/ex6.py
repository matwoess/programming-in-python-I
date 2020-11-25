"""
ex6.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 6
"""
from pathlib import Path
from typing import Tuple


def get_hamsters(folderpath: str) -> Tuple[str, str]:
    files = sorted(Path(folderpath).glob('**/*.raw.seq'))
    yield from ((file.name, file.read_text()) for file in files)


if __name__ == '__main__':
    folder_path = '00'
    file_reader = get_hamsters(folderpath=folder_path)
    # This should print the length of each file content for all sorted files:
    for filename, file_content in file_reader:
        # file content should be the content of the file as string
        print(f'{filename}: {len(file_content)}')
