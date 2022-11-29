from pathlib import Path

p = Path('C:\Program Files')

for i in p.iterdir():
    print(p.exists)