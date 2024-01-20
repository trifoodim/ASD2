class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode

        if ParentNode is None:
            self.Root = NewChild

        else:
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = [self.Root]
        # breadth-first search is used intentionally instead of recursion
        i = 0
        while i < len(nodes):
            nodes += nodes[i].Children
            i += 1
        return nodes

    def FindNodesByValue(self, val):
        return [node for node in self.GetAllNodes() if node.NodeValue == val]

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len([node for node in self.GetAllNodes() if node.Children == []])
