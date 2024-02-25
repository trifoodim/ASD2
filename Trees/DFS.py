class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


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

    def DepthFirstSearch(self, VFrom, VTo):
        assert (self.vertex[VFrom] is not None)
        assert (self.vertex[VTo] is not None)

        stack = _PathStack(self.vertex)
        stack.push(VFrom)
        while not stack.is_empty():
            current = stack.peek()
            if current == VTo:
                return stack.path()
            if stack.is_new_top():
                next = self.__new_vertex_next(current, VTo)
            else:
                next = self.__vertex_next(current)
            if next is None:
                stack.pop()
                continue
            stack.push(next)
        return []

    def WeakVertices(self):
        vertex_indices = [i for i in range(self.max_vertex) \
                          if self.vertex[i] is not None]
        for i in vertex_indices:
            self.vertex[i].Hit = False
        for i in vertex_indices:
            if self.vertex[i].Hit:
                continue
            self.vertex[i].Hit = True
            neighbor_indices = self.__not_visited_neighbors(i)
            if not self.__mark_linked_pairs(neighbor_indices):
                self.vertex[i].Hit = False
        return [v for v in self.vertex if v is not None and not v.Hit]

    def __new_vertex_next(self, start, goal):
        if self.m_adjacency[start][goal]:
            return goal
        return self.__vertex_next(start)

    def __vertex_next(self, start):
        for j in range(self.max_vertex):
            if self.m_adjacency[start][j] == 1 and not self.vertex[j].Hit:
                return j
        return None

    def __not_visited_neighbors(self, start):
        return [j for j in range(self.max_vertex) \
                if self.m_adjacency[start][j] == 1 and not self.vertex[j].Hit]

    def __mark_linked_pairs(self, indices):
        is_marked = False
        for i in range(len(indices)):
            v1 = indices[i]
            for j in range(i + 1, len(indices)):
                v2 = indices[j]
                if self.m_adjacency[v1][v2] == 1:
                    self.vertex[v1].Hit = True
                    self.vertex[v2].Hit = True
                    is_marked = True
        return is_marked


class _Stack:

    def __init__(self):
        self.__values = []

    def push(self, index):
        self.__values.append(index)

    def peek(self):
        return self.__values[-1]

    def pop(self):
        return self.__values.pop()

    def size(self):
        return len(self.__values)

    def values(self):
        return self.__values


class _PathStack:

    def __init__(self, vertex):
        self.__stack = _Stack()
        self.__vertex = vertex
        self.__is_new_top = False
        for v in self.__vertex:
            if v is not None:
                v.Hit = False

    def push(self, index):
        self.__stack.push(index)
        self.__vertex[index].Hit = True
        self.__is_new_top = True

    def peek(self):
        return self.__stack.peek()

    def pop(self):
        self.__is_new_top = False
        self.__stack.pop()

    def is_new_top(self):
        return self.__is_new_top

    def is_empty(self):
        return self.__stack.size() == 0

    def path(self):
        return [self.__vertex[i] for i in self.__stack.values()]
