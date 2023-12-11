class Node:
    def __init__(self, label, val = None):
        self.label  = label
        self.val    = val
        self.parent = None
        self.child  = None

    def getValue(self):
        return self.val
    
    def setValue(self, val):
        self.val = val

    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label

    def getParent(self):
        return self.parent

    def setParent(self, node):
        self.parent = node

    def getChild(self):
        return self.child
    
    def setChild(self, node):
        if self.child is None:
            self.child = node
        else:
            self.child = [self.child, node]

    def __repr__(self):
        return f"Node: {self.label}{f' ({self.val})' if self.val is not None else ''}"


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges

    def getNode(self, label):
        return [node for node in self.nodes if node.getLabel() == label][0]

    def addNode(self, label, val = None):
        self.nodes.append(Node(label, val = val))

    def connectNode(self, parent_label, child_label):
        parent = self.getNode(parent_label)
        child  = self.getNode(child_label)

        parent.setChild(child)
        child.setParent(parent)

        self.edges.append((parent_label, child_label))

if __name__ == '__main__':
    tree = Tree()

    tree.addNode("Ryan", 7)
    tree.addNode("Ben", 6)
    tree.addNode("Christian", 6)
    tree.addNode("Nat", 4)
    tree.addNode("Mike", 5)
    tree.addNode("Travis", 5)

    tree.connectNode("Ryan", "Ben")
    tree.connectNode("Ryan", "Christian")
    tree.connectNode("Ben", "Travis")
    tree.connectNode("Christian", "Nat")
    tree.connectNode("Christian", "Mike")

    print(tree.getEdges())
    print(tree.getNodes())

    for node in tree.nodes:
        print(node)
        print(node.getParent())
        print(node.getChild())