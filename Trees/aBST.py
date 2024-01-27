class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        index = self.__find_index(key, 0)
        if index is None:
            return None
        if self.Tree[index] is None:
            return -index
        return index

    def AddKey(self, key):
        index = self.__find_index(key, 0)
        if index is None:
            return -1
        self.Tree[index] = key
        return index

    def __find_index(self, key, start):
        if start >= len(self.Tree):
            return None
        if self.Tree[start] is None or self.Tree[start] == key:
            return start
        if key < self.Tree[start]:
            return self.__find_index(key, _left_child_index(start))
        return self.__find_index(key, _right_child_index(start))


def _left_child_index(i):
    return 2 * i + 1


def _right_child_index(i):
    return 2 * i + 2
