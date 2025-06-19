from pathlib import Path

def tree_view(path: Path, colors: dict, spacing: str = ''):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{spacing}{colors['dir']}{item.name}/")
                tree_view(item, colors, spacing + '    ')
            else:
                print(f"{spacing}{colors['file']}{item.name}")
    except PermissionError:
        print(f"{spacing}{colors['error']}Permission denied: {path}")
