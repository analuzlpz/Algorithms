class Graph:
    def __init__(self, vertices, arcos, relations, abs_distance):
        self.Vert_count = vertices
        self.Edges_count = arcos
        self.relations = relations
        self.abs_distance = abs_distance

    def print_graph(self):
        print("Vert ", self.Vert_count)
        print("Edge ", self.Edges_count)
        print("Relations ", self.relations)
        print("Abs distance ", self.abs_distance)

    def shortest_reach(self, start):
        dist = [None] * self.Vert_count
        visited = [False] * self.Vert_count

        dist[start] = 0

        for vert in range(self.Vert_count):
            visited[vert] = True
            if vert == start:
                dist[vert] = 0

            if self.relations.get(vert) is None:
                continue

            for vert2 in range(self.Vert_count):
                if vert2 == start:
                    continue
                if vert2 in self.relations.get(vert):
                    if dist[vert] is None or dist[vert] == 0:
                        dist[vert2] = 6
                    else:
                        dist[vert2] = dist[vert] + 6

        print(dist)


vertices = 6
arcs = 4
relations = {0: [1, 4], 1: [2], 2: [3]}
abs_distance = 6

graph = Graph(vertices, arcs, relations, abs_distance)
graph.print_graph()
graph.shortest_reach(0)
