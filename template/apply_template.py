from pathlib import Path
import shutil

YEAR = 2021

for day in range(10, 14):
    target = Path(f'../{YEAR}/day{day:02d}')
    shutil.copytree('../template', target)
    content = (target / 'solution.ipynb').read_text()
    (target / 'solution.ipynb').write_text(content.replace('YYYY', f'{YEAR}').replace('DD', f'{day}'))
    (target / 'apply_template.py').unlink()
