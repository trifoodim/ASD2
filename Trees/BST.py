class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        return _find(self.Root, key)

    def AddKeyValue(self, key, val):
        f = self.FindNodeByKey(key)
        if f.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        if f.NodeHasKey:
            return False
        if f.ToLeft:
            f.Node.LeftChild = BSTNode(key, val, f.Node)
            return True
        f.Node.RightChild = BSTNode(key, val, f.Node)
        return True

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax:
            get_next_node = lambda n: n.RightChild
        else:
            get_next_node = lambda n: n.LeftChild
        while True:
            next = get_next_node(node)
            if next is None:
                return node
            node = next

    def DeleteNodeByKey(self, key):
        f = self.FindNodeByKey(key)
        if not f.NodeHasKey:
            return False
        node_parent = f.Node.Parent
        self.__detach_node(f.Node)
        if f.Node.RightChild is None and f.Node.LeftChild is None:
            return True
        if f.Node.LeftChild is None:
            self.__move_node(f.Node.RightChild, node_parent)
            return True
        if f.Node.RightChild is None:
            self.__move_node(f.Node.LeftChild, node_parent)
            return True
        successor_node = self.FinMinMax(f.Node.RightChild, False)

        successor_parent = successor_node.Parent
        self.__detach_node(successor_node)
        if successor_node.RightChild is not None and successor_parent is not f.Node:
            self.__move_node(successor_node.RightChild, successor_parent)
        self.__attach_node(successor_node, node_parent)

        if f.Node.RightChild is not None:
            self.__move_node(f.Node.RightChild, successor_node)
        self.__move_node(f.Node.LeftChild, successor_node)
        return True

    def Count(self):
        return _count(self.Root)

    def __move_node(self, node, new_parent):
        self.__detach_node(node)
        self.__attach_node(node, new_parent)

    def __detach_node(self, node):
        if node.Parent is None:
            self.Root = None
        elif node.Parent.LeftChild == node:
            node.Parent.LeftChild = None
        else:
            node.Parent.RightChild = None
        node.Parent = None

    def __attach_node(self, node, new_parent):
        node.Parent = new_parent
        if new_parent is None:
            self.Root = node
        elif node.NodeKey < new_parent.NodeKey:
            new_parent.LeftChild = node
        else:
            new_parent.RightChild = node


def _find(node, key):
    if key == node.NodeKey:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = True
        return f
    if key < node.NodeKey:
        return _find_left(node, key)
    return _find_right(node, key)


def _find_left(node, key):
    if node.LeftChild is None:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = False
        f.ToLeft = True
        return f
    return _find(node.LeftChild, key)


def _find_right(node, key):
    if node.RightChild is None:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = False
        f.ToLeft = False
        return f
    return _find(node.RightChild, key)


def _count(node):
    if node is None:
        return 0
    return _count(node.LeftChild) + 1 + _count(node.RightChild)