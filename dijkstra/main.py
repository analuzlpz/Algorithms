from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None


if __name__ == "__main__":
    edges = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("A", "E", 7),
        ("B", "C", 6),
        ("B", "A", 4),
        ("B", "D", 5),
        ("C", "A", 3),
        ("C", "B", 6),
        ("C", "D", 11),
        ("C", "E", 8),
        ("D", "B", 5),
        ("D", "C", 11),
        ("D", "E", 2),
        ("D", "G", 10),
        ("D", "F", 2),
        ("E", "A", 7),
        ("E", "C", 8),
        ("E", "E", 2),
        ("E", "G", 5),
        ("G", "E", 5),
        ("G", "D", 10),
        ("G", "F", 3),
        ("F", "D", 2),
        ("F", "G", 3),
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> F:")
    print(dijkstra(edges, "A", "F"))
    print("F -> G:")
    print(dijkstra(edges, "F", "G"))
