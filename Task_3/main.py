import sys
from pathlib import Path
from colorama import init
from tree_view.tree_view import tree_view
from utils.color_theme import COLORS

init(autoreset=True)

def main():
    if len(sys.argv) != 2:
        print(f"{COLORS['warning']}Please provide a directory path as a command-line argument.")
        sys.exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print(f"{COLORS['error']}The path does not exist: {root_path}")
        sys.exit(1)

    if not root_path.is_dir():
        print(f"{COLORS['error']}The path is not a directory: {root_path}")
        sys.exit(1)

    print(f"{COLORS['title']}Directory structure of {root_path}:\n")
    tree_view(root_path, COLORS)

if __name__ == "__main__":
    main()
