import sys
from pathlib import Path

from src.graph_project.graph import Graph


def run_checks(graph: Graph) -> None:
    graph.is_connected()
    graph.has_cycles()
    graph.is_tree()
    graph.is_forest()


def main() -> None:
    
    if len(sys.argv) > 1:
        files = [Path(arg) for arg in sys.argv[1:]]
    else:
        files = sorted(Path("data").glob("*.txt"))

    for file_path in files:
        print(f"=== {file_path} ===")

        print("--- Undirected graph ---")
        run_checks(Graph.load_from_file(str(file_path), is_directed=False))

        print("--- Directed graph ---")
        run_checks(Graph.load_from_file(str(file_path), is_directed=True))
        print()


if __name__ == "__main__":
    main()
