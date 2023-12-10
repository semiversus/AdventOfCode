from pathlib import Path
import shutil

def add(year: int, day: int):
    target = Path(f'../{year}/day{day:02d}')
    shutil.copytree('../template', target)
    content = (target / 'solution.ipynb').read_text()
    (target / 'solution.ipynb').write_text(content.replace('YYYY', f'{year}').replace('DD', f'{day}'))
    (target / 'apply_template.py').unlink()

if __name__ == '__main__':
    from sys import argv
    if len(argv) != 3:
        print('need YEAR and DAY as arguments')
    year, day = int(argv[1]), int(argv[2])
    add(year, day)