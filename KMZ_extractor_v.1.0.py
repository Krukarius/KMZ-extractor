import os, sys, zipfile

for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
  base_file, ext = os.path.splitext(filename)
  if ext == ".kmz":
    os.rename(filename, base_file + ".zip")

from pathlib import Path
p = Path(__file__).parent.absolute()
for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=f'./{f.stem}')
        print(f'Done {f.stem}')

dir_name = p
test = os.listdir(dir_name)
for item in test:
    if item.endswith(".zip"):
        os.remove(os.path.join(dir_name, item))
