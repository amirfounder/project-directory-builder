from pathlib import Path
from src.project_builder import build_project


def main():
    project_root = Path(__file__).parent
    project_root = str(project_root)
    build_project(project_root)


if __name__ == '__main__':
    main()
    