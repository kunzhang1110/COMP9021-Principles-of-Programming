import os
import re

directory = 'names'
folder = os.listdir(directory)
print(folder)
for filename in folder:
    if not filename.endswith('.txt'):
        continue
    match = re.search(r'\d{4}', filename)
    year = match.group()
