class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def EvenTrees(self):
        if self.Root is None:
            return []
        even_trees = _find_even_trees(self.Root)
        if even_trees.num_remaining_vertices % 2 != 0:
            return []
        return even_trees.edges_to_remove


class _EvenTrees:

    def __init__(self, edges_to_remove, num_remaining_vertices):
        self.edges_to_remove = edges_to_remove
        self.num_remaining_vertices = num_remaining_vertices


def _find_even_trees(root):
    assert (root is not None)
    edges_to_remove = []
    num_remaining_vertices = 0
    for child in root.Children:
        even_trees = _find_even_trees(child)
        assert (even_trees.num_remaining_vertices > 0)
        if even_trees.num_remaining_vertices % 2 == 0:
            edges_to_remove += [root, child]
        else:
            num_remaining_vertices += even_trees.num_remaining_vertices
        edges_to_remove += even_trees.edges_to_remove
    return _EvenTrees(edges_to_remove, num_remaining_vertices + 1)
