from typing import List, Optional

class BSTNode:

    def __init__(self, key: int, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a: List):
        sorted_array = sorted(a)
        self.Root = _build_tree(sorted_array, None, 0)

    def IsBalanced(self, root_node: Optional[BSTNode]):
        return _get_balanced_depth(root_node) is not None


def _build_tree(sorted_array: List, parent: BSTNode, level: int):
    if len(sorted_array) == 0:
        return None
    mid = len(sorted_array) // 2
    node = BSTNode(sorted_array[mid], parent)
    node.Level = level
    node.LeftChild = _build_tree(sorted_array[:mid], node, level + 1)
    node.RightChild = _build_tree(sorted_array[mid + 1:], node, level + 1)
    return node


def _get_balanced_depth(node: BSTNode):
    if node is None:
        return 0
    left_depth = _get_balanced_depth(node.LeftChild)
    right_depth = _get_balanced_depth(node.RightChild)
    if left_depth is None or right_depth is None:
        return None
    if abs(left_depth - right_depth) > 1:
        return None
    return max(left_depth, right_depth) + 1