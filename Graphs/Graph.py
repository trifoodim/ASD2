class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int) -> None:
        new_vertex = Vertex(v)
        new_index = 0
        while new_index < self.max_vertex:
            if not self.vertex[new_index]:
                break
            new_index += 1
        self.vertex[new_index] = new_vertex
        j = 0
        while j <= new_index:
            self.m_adjacency[j][new_index] = 0
            self.m_adjacency[new_index][j] = 0
            j += 1

    def RemoveVertex(self, v: int) -> None:
        i = v
        while i < self.max_vertex - 1:
            self.vertex[i] = self.vertex[i + 1]
            i += 1
        self.vertex[self.max_vertex - 1] = None
        x = 0

        while x < self.max_vertex - 1:
            y = v + 1
            while y < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y + 1][x]
                y += 1
            x += 1

        y = 0
        while y < self.max_vertex - 1:
            x = v + 1
            while x < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y][x + 1]
                x += 1
            y += 1

    def IsEdge(self, v1, v2):
        return True if self.m_adjacency[v1][v2] == 1 else False

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
